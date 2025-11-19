"""
Agent状态定义
"""
from typing import List, Dict, Any, Optional, Annotated
from pydantic import BaseModel, Field
from langgraph.graph import add_messages
from langchain_core.messages import BaseMessage


class AgentState(BaseModel):
    """Agent状态类"""
    
    # 消息历史
    messages: Annotated[List[BaseMessage], add_messages] = Field(default_factory=list)
    
    # 当前任务
    current_task: Optional[str] = None
    
    # 任务历史
    task_history: List[str] = Field(default_factory=list)
    
    # 工具调用结果
    tool_results: Dict[str, Any] = Field(default_factory=dict)
    
    # 迭代计数
    iteration_count: int = 0
    
    # 最大迭代次数
    max_iterations: int = 10
    
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
