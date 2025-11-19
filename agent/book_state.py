"""
图书推荐Agent状态定义
"""
from typing import List, Dict, Any, Optional, Annotated
from pydantic import BaseModel, Field
from langgraph.graph import add_messages
from langchain_core.messages import BaseMessage


class BookInfo(BaseModel):
    """图书信息模型"""
    title: str
    author: str
    isbn: Optional[str] = None
    genre: Optional[str] = None
    rating: Optional[float] = None
    description: Optional[str] = None
    publication_year: Optional[int] = None
    publisher: Optional[str] = None


class UserPreference(BaseModel):
    """用户偏好模型"""
    favorite_genres: List[str] = Field(default_factory=list)
    favorite_authors: List[str] = Field(default_factory=list)
    reading_history: List[BookInfo] = Field(default_factory=list)
    preferred_rating: Optional[float] = None
    preferred_years: Optional[List[int]] = None


class BookRecommendationState(BaseModel):
    """图书推荐Agent状态"""
    
    # 消息历史
    messages: Annotated[List[BaseMessage], add_messages] = Field(default_factory=list)
    
    # 用户信息
    user_id: Optional[str] = None
    user_preferences: Optional[UserPreference] = None
    
    # 当前浏览的图书
    current_book: Optional[BookInfo] = None
    
    # 推荐结果
    recommendations: List[BookInfo] = Field(default_factory=list)
    
    # 推荐原因
    recommendation_reasons: List[str] = Field(default_factory=list)
    
    # 知识图谱数据
    knowledge_graph: Dict[str, Any] = Field(default_factory=dict)
    
    # 搜索历史
    search_history: List[str] = Field(default_factory=list)
    
    # 迭代计数
    iteration_count: int = 0
    max_iterations: int = 5
    
    # 是否完成
    is_finished: bool = False
    
    # 错误信息
    error_message: Optional[str] = None
    
    # 用户输入
    user_input: Optional[str] = None
    
    # 最终结果
    final_result: Optional[str] = None
    
    class Config:
        arbitrary_types_allowed = True