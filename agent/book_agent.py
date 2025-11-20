"""
图书推荐Agent实现
"""
import json
from collections import Counter, defaultdict
from typing import Dict, Any, List, Optional, Tuple
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage, ToolMessage
from langchain_core.tools import tool
from langgraph.graph import StateGraph, END
from langgraph.prebuilt import ToolNode
from langgraph.graph.message import add_messages

from book_state import BookRecommendationState, BookInfo, UserPreference
from book_tools import book_recommendation_tool, book_search_tool, book_analysis_tool
from config import DEEPSEEK_API_KEY, AGENT_MODEL, TEMPERATURE, DEEPSEEK_BASE_URL


# 创建LLM实例 - 使用DeepSeek
llm = ChatOpenAI(
    api_key=DEEPSEEK_API_KEY,
    model=AGENT_MODEL,
    temperature=TEMPERATURE,
    base_url=DEEPSEEK_BASE_URL
)


# 定义图书相关工具
@tool
def search_books(query: str, limit: int = 10) -> str:
    """搜索图书"""
    result = book_search_tool.search_books(query, limit)
    return json.dumps(result, ensure_ascii=False)


@tool
def get_book_details(title: str) -> str:
    """获取图书详细信息"""
    result = book_search_tool.get_book_details(title)
    return json.dumps(result, ensure_ascii=False)


@tool
def recommend_by_author(author: str, exclude_books: str = "[]") -> str:
    """根据作者推荐图书"""
    exclude_list = json.loads(exclude_books) if exclude_books else []
    result = book_recommendation_tool.recommend_by_author(author, exclude_list)
    return json.dumps(result, ensure_ascii=False)


@tool
def recommend_by_genre(genre: str, exclude_books: str = "[]") -> str:
    """根据类型推荐图书"""
    exclude_list = json.loads(exclude_books) if exclude_books else []
    result = book_recommendation_tool.recommend_by_genre(genre, exclude_list)
    return json.dumps(result, ensure_ascii=False)


@tool
def recommend_by_knowledge_graph(book_info: str) -> str:
    """基于知识图谱推荐图书"""
    book_data = json.loads(book_info)
    result = book_recommendation_tool.recommend_by_knowledge_graph(book_data)
    return json.dumps(result, ensure_ascii=False)


@tool
def get_user_preferences(user_id: str) -> str:
    """获取用户偏好"""
    result = book_recommendation_tool.get_user_preferences(user_id)
    return json.dumps(result, ensure_ascii=False)


@tool
def update_user_preferences(user_id: str, book_info: str) -> str:
    """更新用户偏好"""
    book_data = json.loads(book_info)
    result = book_recommendation_tool.update_user_preferences(user_id, book_data)
    return json.dumps(result, ensure_ascii=False)


@tool
def analyze_reading_trends(user_history: str) -> str:
    """分析用户阅读趋势"""
    history_data = json.loads(user_history)
    result = book_analysis_tool.analyze_reading_trends(history_data)
    return json.dumps(result, ensure_ascii=False)


@tool
def get_similar_books(book_info: str) -> str:
    """获取相似图书"""
    book_data = json.loads(book_info)
    result = book_analysis_tool.get_similar_books(book_data)
    return json.dumps(result, ensure_ascii=False)


# 工具列表
book_tools = [
    search_books,
    get_book_details,
    recommend_by_author,
    recommend_by_genre,
    recommend_by_knowledge_graph,
    get_user_preferences,
    update_user_preferences,
    analyze_reading_trends,
    get_similar_books
]

# 绑定工具到LLM
llm_with_tools = llm.bind_tools(book_tools)


def should_continue(state: BookRecommendationState) -> str:
    """决定是否继续执行"""
    messages = state.messages
    
    # 检查是否达到最大迭代次数
    if state.iteration_count >= state.max_iterations:
        return "end"
    
    # 检查最后一条消息是否是工具调用
    last_message = messages[-1]
    if hasattr(last_message, 'tool_calls') and last_message.tool_calls:
        return "tools"
    else:
        return "end"


def call_model(state: BookRecommendationState) -> Dict[str, Any]:
    """调用模型生成响应"""
    messages = state.messages
    
    # 添加系统消息
    system_message = SystemMessage(content="""
    你是一个专业的图书推荐助手，可以帮助用户：
    1. 搜索图书信息
    2. 根据用户浏览的图书推荐相似图书
    3. 基于知识图谱进行智能推荐
    4. 分析用户阅读偏好
    5. 提供个性化的图书推荐
    
    你可以使用以下工具：
    - search_books: 搜索图书
    - get_book_details: 获取图书详细信息
    - recommend_by_author: 根据作者推荐图书
    - recommend_by_genre: 根据类型推荐图书
    - recommend_by_knowledge_graph: 基于知识图谱推荐
    - get_user_preferences: 获取用户偏好
    - update_user_preferences: 更新用户偏好
    - analyze_reading_trends: 分析阅读趋势
    - get_similar_books: 获取相似图书
    
    请根据用户的需求选择合适的工具，并提供有用的图书推荐。
    推荐时请说明推荐理由，并考虑用户的阅读偏好。
    """)
    
    # 构建消息列表
    preference_hint = getattr(state, "preference_hint", None)
    if preference_hint:
        preference_message = SystemMessage(content=preference_hint)
        all_messages = [system_message, preference_message] + messages
    else:
        all_messages = [system_message] + messages
    
    # 调用模型
    response = llm_with_tools.invoke(all_messages)
    
    return {"messages": [response]}


def call_tools(state: BookRecommendationState) -> Dict[str, Any]:
    """调用工具"""
    messages = state.messages
    last_message = messages[-1]
    
    # 创建工具节点
    tool_node = ToolNode(book_tools)
    
    # 调用工具
    tool_messages = tool_node.invoke({"messages": [last_message]})
    
    return {"messages": tool_messages["messages"]}


def create_book_agent_graph() -> StateGraph:
    """创建图书推荐Agent图"""
    
    # 创建状态图
    workflow = StateGraph(BookRecommendationState)
    
    # 添加节点
    workflow.add_node("agent", call_model)
    workflow.add_node("tools", call_tools)
    
    # 设置入口点
    workflow.set_entry_point("agent")
    
    # 添加条件边
    workflow.add_conditional_edges(
        "agent",
        should_continue,
        {
            "tools": "tools",
            "end": END
        }
    )
    
    # 从工具回到agent
    workflow.add_edge("tools", "agent")
    
    return workflow


class BookRecommendationAgent:
    """图书推荐Agent类"""
    
    def __init__(self):
        self.graph = create_book_agent_graph().compile()
        self.conversation_history = defaultdict(list)
        self._prepare_metadata()
        self.max_history_entries = 50
        self.recent_window = 5
    
    def _prepare_metadata(self) -> None:
        """预处理作者、类型、书名等元数据，便于快速抽取偏好"""
        books = book_recommendation_tool.db.books
        author_set = {book.get("author") for book in books if book.get("author")}
        genre_set = {book.get("genre") for book in books if book.get("genre")}
        self.author_entries = [(author, author.lower()) for author in sorted(author_set, key=len, reverse=True)]
        self.genre_entries = [(genre, genre.lower()) for genre in sorted(genre_set, key=len, reverse=True)]
        title_set = {book.get("title") for book in books if book.get("title")}
        self.title_entries = [(title, title.lower()) for title in sorted(title_set, key=len, reverse=True)]
        self.title_lookup: Dict[str, Dict[str, Any]] = {}
        for book in books:
            title = book.get("title")
            if title:
                self.title_lookup[title.lower()] = book
    
    def _normalize_user_id(self, user_id: Optional[str]) -> str:
        return user_id or "anonymous_user"
    
    def _append_history(self, user_id: str, entry: Dict[str, Any]) -> None:
        history = self.conversation_history[user_id]
        history.append(entry)
        if len(history) > self.max_history_entries:
            self.conversation_history[user_id] = history[-self.max_history_entries:]
    
    def _extract_entities(self, text: str) -> Tuple[List[str], List[str], List[str]]:
        if not text:
            return [], [], []
        text_lower = text.lower()
        authors = {raw for raw, lower in self.author_entries if lower in text_lower}
        genres = {raw for raw, lower in self.genre_entries if lower in text_lower}
        titles = {raw for raw, lower in self.title_entries if lower in text_lower}
        
        # 通过书名自动补全作者/类型偏好
        for title in titles:
            book = self.title_lookup.get(title.lower())
            if not book:
                continue
            author = book.get("author")
            genre = book.get("genre")
            if author:
                authors.add(author)
            if genre:
                genres.add(genre)
        
        return sorted(authors), sorted(genres), sorted(titles)
    
    def _record_user_message(self, user_id: Optional[str], content: str) -> None:
        normalized_id = self._normalize_user_id(user_id)
        authors, genres, titles = self._extract_entities(content)
        entry = {
            "role": "user",
            "content": content,
            "authors": authors,
            "genres": genres,
            "titles": titles
        }
        self._append_history(normalized_id, entry)
    
    def _record_ai_message(self, user_id: Optional[str], content: str) -> None:
        normalized_id = self._normalize_user_id(user_id)
        entry = {
            "role": "assistant",
            "content": content
        }
        self._append_history(normalized_id, entry)
    
    def _extract_last_ai_message(self, messages: List[Any]) -> Optional[str]:
        for message in reversed(messages or []):
            if isinstance(message, AIMessage):
                return message.content
        return None
    
    def _build_preference_hint(self, user_id: Optional[str]) -> Optional[str]:
        normalized_id = self._normalize_user_id(user_id)
        history = self.conversation_history.get(normalized_id, [])
        user_entries = [entry for entry in history if entry.get("role") == "user"]
        if not user_entries:
            return None
        
        recent_entries = user_entries[-self.recent_window:]
        author_counter = Counter()
        genre_counter = Counter()
        for entry in recent_entries:
            for author in entry.get("authors", []):
                author_counter[author] += 1
            for genre in entry.get("genres", []):
                genre_counter[genre] += 1
        
        if not author_counter and not genre_counter:
            return None
        
        hint_lines = ["请结合以下会话偏好优先推荐相关图书，并在回复中明确指出是“因为你之前提到过……所以优先推荐……”。"]
        if author_counter:
            top_authors = [name for name, _ in author_counter.most_common(3)]
            hint_lines.append(f"- 最近关注的作者：{', '.join(top_authors)}")
        if genre_counter:
            top_genres = [name for name, _ in genre_counter.most_common(3)]
            hint_lines.append(f"- 最近关注的类型：{', '.join(top_genres)}")
        hint_lines.append("若新的推荐满足这些偏好，请在回复中显式说明这一理由。")
        return "\n".join(hint_lines)
    
    def _post_interaction(self, user_id: Optional[str], user_input: str, final_messages: List[Any]) -> None:
        self._record_user_message(user_id, user_input)
        response = self._extract_last_ai_message(final_messages)
        if response:
            self._record_ai_message(user_id, response)
    
    def run(
        self,
        user_input: str,
        user_id: str = None,
        max_iterations: int = 5,
        preference_hint: Optional[str] = None
    ) -> Dict[str, Any]:
        """运行图书推荐Agent"""
        
        # 创建初始状态
        initial_state = BookRecommendationState(
            messages=[HumanMessage(content=user_input)],
            user_input=user_input,
            user_id=user_id,
            max_iterations=max_iterations,
            iteration_count=0,
            preference_hint=preference_hint
        )
        
        # 运行图
        final_state = self.graph.invoke(initial_state)
        
        # 提取结果
        result = {
            "user_input": user_input,
            "user_id": user_id,
            "final_messages": final_state.get('messages', []),
            "recommendations": final_state.get('recommendations', []),
            "recommendation_reasons": final_state.get('recommendation_reasons', []),
            "iteration_count": final_state.get('iteration_count', 0),
            "is_finished": final_state.get('is_finished', False),
            "error_message": final_state.get('error_message')
        }
        
        return result
    
    def chat(self, message: str, user_id: str = None) -> str:
        """简单的聊天接口"""
        preference_hint = self._build_preference_hint(user_id)
        result = self.run(message, user_id, preference_hint=preference_hint)
        messages = result.get("final_messages", [])
        response = self._extract_last_ai_message(messages)
        self._post_interaction(user_id, message, messages)
        
        if response:
            return response
        return "抱歉，我无法处理您的图书推荐请求。"
    
    def recommend_books(self, book_title: str, user_id: str = None) -> Dict[str, Any]:
        """推荐图书的专门方法"""
        query = f"我浏览了图书《{book_title}》，请为我推荐相似的图书"
        preference_hint = self._build_preference_hint(user_id)
        result = self.run(query, user_id, preference_hint=preference_hint)
        self._post_interaction(user_id, query, result.get("final_messages", []))
        return result
    
    def search_and_recommend(self, search_query: str, user_id: str = None) -> Dict[str, Any]:
        """搜索并推荐图书"""
        query = f"搜索图书：{search_query}，然后为我推荐相关图书"
        preference_hint = self._build_preference_hint(user_id)
        result = self.run(query, user_id, preference_hint=preference_hint)
        self._post_interaction(user_id, query, result.get("final_messages", []))
        return result