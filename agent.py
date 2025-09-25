"""
基于LangGraph的Agent实现
"""
import json
from typing import Dict, Any, List
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage, ToolMessage
from langchain_core.tools import tool
from langgraph.graph import StateGraph, END
from langgraph.prebuilt import ToolNode
from langgraph.graph.message import add_messages

from state import AgentState
from tools import TOOLS
from config import OPENAI_API_KEY, AGENT_MODEL, TEMPERATURE, MAX_ITERATIONS


# 创建LLM实例
llm = ChatOpenAI(
    api_key=OPENAI_API_KEY,
    model=AGENT_MODEL,
    temperature=TEMPERATURE
)


# 定义工具
@tool
def calculator(expression: str) -> str:
    """计算数学表达式"""
    result = TOOLS["calculator"].calculate(expression)
    return json.dumps(result, ensure_ascii=False)


@tool
def web_search(query: str, num_results: int = 5) -> str:
    """搜索网络信息"""
    result = TOOLS["web_search"].search(query, num_results)
    return json.dumps(result, ensure_ascii=False)


@tool
def read_file(file_path: str) -> str:
    """读取文件内容"""
    result = TOOLS["file"].read_file(file_path)
    return json.dumps(result, ensure_ascii=False)


@tool
def write_file(file_path: str, content: str) -> str:
    """写入文件内容"""
    result = TOOLS["file"].write_file(file_path, content)
    return json.dumps(result, ensure_ascii=False)


@tool
def list_files(directory: str = ".") -> str:
    """列出目录中的文件"""
    result = TOOLS["file"].list_files(directory)
    return json.dumps(result, ensure_ascii=False)


@tool
def create_chart(data: str, chart_type: str = "line") -> str:
    """创建数据分析图表"""
    try:
        data_list = json.loads(data)
        result = TOOLS["data_analysis"].create_chart(data_list, chart_type)
        return json.dumps(result, ensure_ascii=False)
    except Exception as e:
        return json.dumps({"success": False, "error": str(e)}, ensure_ascii=False)


@tool
def analyze_data(data: str) -> str:
    """分析数据统计信息"""
    try:
        data_list = json.loads(data)
        result = TOOLS["data_analysis"].analyze_data(data_list)
        return json.dumps(result, ensure_ascii=False)
    except Exception as e:
        return json.dumps({"success": False, "error": str(e)}, ensure_ascii=False)


@tool
def get_current_time() -> str:
    """获取当前时间"""
    result = TOOLS["time"].get_current_time()
    return json.dumps(result, ensure_ascii=False)


# 工具列表
tools = [
    calculator,
    web_search,
    read_file,
    write_file,
    list_files,
    create_chart,
    analyze_data,
    get_current_time
]

# 绑定工具到LLM
llm_with_tools = llm.bind_tools(tools)


def should_continue(state: AgentState) -> str:
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


def call_model(state: AgentState) -> Dict[str, Any]:
    """调用模型生成响应"""
    messages = state.messages
    
    # 添加系统消息
    system_message = SystemMessage(content="""
    你是一个智能助手，可以帮助用户完成各种任务。
    你可以使用以下工具：
    - calculator: 计算数学表达式
    - web_search: 搜索网络信息
    - read_file: 读取文件
    - write_file: 写入文件
    - list_files: 列出文件
    - create_chart: 创建图表
    - analyze_data: 分析数据
    - get_current_time: 获取当前时间
    
    请根据用户的需求选择合适的工具，并给出有用的回答。
    """)
    
    # 构建消息列表
    all_messages = [system_message] + messages
    
    # 调用模型
    response = llm_with_tools.invoke(all_messages)
    
    return {"messages": [response]}


def call_tools(state: AgentState) -> Dict[str, Any]:
    """调用工具"""
    messages = state.messages
    last_message = messages[-1]
    
    # 创建工具节点
    tool_node = ToolNode(tools)
    
    # 调用工具
    tool_messages = tool_node.invoke({"messages": [last_message]})
    
    return {"messages": tool_messages["messages"]}


def create_agent_graph() -> StateGraph:
    """创建Agent图"""
    
    # 创建状态图
    workflow = StateGraph(AgentState)
    
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


class LangGraphAgent:
    """LangGraph Agent类"""
    
    def __init__(self):
        self.graph = create_agent_graph().compile()
    
    def run(self, user_input: str, max_iterations: int = MAX_ITERATIONS) -> Dict[str, Any]:
        """运行Agent"""
        
        # 创建初始状态
        initial_state = AgentState(
            messages=[HumanMessage(content=user_input)],
            user_input=user_input,
            max_iterations=max_iterations,
            iteration_count=0
        )
        
        # 运行图
        final_state = self.graph.invoke(initial_state)
        
        # 提取结果
        result = {
            "user_input": user_input,
            "final_messages": final_state.messages,
            "iteration_count": final_state.iteration_count,
            "is_finished": final_state.is_finished,
            "error_message": final_state.error_message
        }
        
        return result
    
    def chat(self, message: str) -> str:
        """简单的聊天接口"""
        result = self.run(message)
        
        # 提取最后一条AI消息
        messages = result["final_messages"]
        for message in reversed(messages):
            if isinstance(message, AIMessage):
                return message.content
        
        return "抱歉，我无法处理您的请求。"
