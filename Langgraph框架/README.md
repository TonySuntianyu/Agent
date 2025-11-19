# LangGraph Agent 框架

一个基于LangGraph构建的智能Agent框架，支持多种工具和复杂的工作流程。

## 功能特性

- 🤖 **智能对话**: 基于OpenAI GPT模型的自然语言交互
- 🛠️ **丰富工具**: 内置计算器、文件操作、数据分析、网络搜索等工具
- 🔄 **工作流管理**: 使用LangGraph实现复杂的Agent工作流
- 📊 **数据分析**: 支持数据统计分析和图表生成
- 🌐 **网络搜索**: 集成网络搜索功能
- 📁 **文件操作**: 支持文件读写和目录管理
- ⏰ **时间工具**: 时间查询和格式化功能

## 项目结构

```
codes/
├── requirements.txt          # 依赖包列表
├── config.py                # 配置文件
├── state.py                 # Agent状态定义
├── tools.py                 # 工具函数集合
├── agent.py                 # 核心Agent实现
├── example.py               # 使用示例
├── test_agent.py            # 测试文件
└── README.md                # 项目文档
```

## 安装和配置

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 配置环境变量

创建 `.env` 文件并设置以下变量：

```env
# OpenAI API配置
OPENAI_API_KEY=your_openai_api_key_here

# 其他API配置（可选）
SERPER_API_KEY=your_serper_api_key_here
WOLFRAM_ALPHA_APPID=your_wolfram_alpha_appid_here

# Agent配置
AGENT_MODEL=gpt-4
TEMPERATURE=0.7
MAX_ITERATIONS=10
```

### 3. 运行示例

```bash
python example.py
```

## 核心组件

### AgentState (状态管理)

```python
class AgentState(BaseModel):
    messages: List[BaseMessage]           # 消息历史
    current_task: Optional[str]          # 当前任务
    task_history: List[str]              # 任务历史
    tool_results: Dict[str, Any]         # 工具调用结果
    iteration_count: int                 # 迭代计数
    max_iterations: int                  # 最大迭代次数
    is_finished: bool                    # 是否完成
    error_message: Optional[str]         # 错误信息
    user_input: Optional[str]            # 用户输入
    final_result: Optional[str]          # 最终结果
```

### 工具集合

#### 1. 计算器工具 (CalculatorTool)
- 安全的数学表达式计算
- 支持基本运算和数学函数

#### 2. 网络搜索工具 (WebSearchTool)
- 集成Serper API进行网络搜索
- 支持搜索结果摘要

#### 3. 文件操作工具 (FileTool)
- 文件读写操作
- 目录文件列表
- 文件管理功能

#### 4. 数据分析工具 (DataAnalysisTool)
- 数据统计分析
- 图表生成
- 支持多种图表类型

#### 5. 时间工具 (TimeTool)
- 当前时间获取
- 时间戳格式化
- 时间转换功能

### LangGraph工作流

```python
# 创建Agent图
workflow = StateGraph(AgentState)

# 添加节点
workflow.add_node("agent", call_model)
workflow.add_node("tools", call_tools)

# 设置条件边
workflow.add_conditional_edges(
    "agent",
    should_continue,
    {
        "tools": "tools",
        "end": END
    }
)
```

## 使用方法

### 基本使用

```python
from agent import LangGraphAgent

# 创建Agent实例
agent = LangGraphAgent()

# 简单对话
response = agent.chat("计算 2^10 + 3*5 的结果")
print(response)

# 复杂任务
response = agent.chat("分析数据 [1,2,3,4,5,6,7,8,9,10] 的统计信息")
print(response)
```

### 交互式聊天

```python
from example import interactive_chat

# 启动交互式聊天
interactive_chat()
```

### 运行测试

```python
from test_agent import run_tests

# 运行所有测试
run_tests()
```

## 工具使用示例

### 数学计算

```python
# 基本计算
agent.chat("计算 2 + 3 * 4")

# 复杂表达式
agent.chat("计算 sin(π/2) + cos(0)")

# 科学计算
agent.chat("计算 2^10 + sqrt(144)")
```

### 文件操作

```python
# 列出文件
agent.chat("列出当前目录的文件")

# 读取文件
agent.chat("读取文件 config.py 的内容")

# 写入文件
agent.chat("创建一个名为 test.txt 的文件，内容为 'Hello World'")
```

### 数据分析

```python
# 数据统计
data = [{"value": i} for i in range(1, 11)]
agent.chat(f"分析数据 {json.dumps(data)} 的统计信息")

# 创建图表
agent.chat(f"为数据 {json.dumps(data)} 创建折线图")
```

### 时间查询

```python
# 获取当前时间
agent.chat("现在几点了？")

# 时间格式化
agent.chat("获取当前时间的Unix时间戳")
```

## 高级功能

### 自定义工具

```python
from langchain_core.tools import tool

@tool
def custom_tool(input_text: str) -> str:
    """自定义工具"""
    # 实现自定义逻辑
    return f"处理结果: {input_text}"

# 添加到工具列表
tools.append(custom_tool)
```

### 状态管理

```python
# 获取Agent状态
state = agent.get_state()

# 检查迭代次数
if state.iteration_count >= state.max_iterations:
    print("达到最大迭代次数")
```

### 错误处理

```python
try:
    result = agent.run("复杂任务")
    if result["error_message"]:
        print(f"错误: {result['error_message']}")
except Exception as e:
    print(f"异常: {e}")
```

## 配置选项

### 模型配置

```python
# 在config.py中修改
AGENT_MODEL = "gpt-4"          # 模型名称
TEMPERATURE = 0.7              # 温度参数
MAX_ITERATIONS = 10             # 最大迭代次数
```

### 工具配置

```python
# 启用/禁用特定工具
ENABLED_TOOLS = [
    "calculator",
    "file",
    "time"
]
```

## 故障排除

### 常见问题

1. **API密钥错误**
   ```
   错误: 请设置OPENAI_API_KEY环境变量
   解决: 检查.env文件或环境变量设置
   ```

2. **依赖包缺失**
   ```
   错误: ModuleNotFoundError
   解决: 运行 pip install -r requirements.txt
   ```

3. **工具调用失败**
   ```
   错误: 工具执行失败
   解决: 检查工具参数和权限设置
   ```

### 调试模式

```python
# 启用详细日志
import logging
logging.basicConfig(level=logging.DEBUG)

# 查看Agent状态
print(agent.get_state())
```

## 贡献指南

1. Fork 项目
2. 创建功能分支
3. 提交更改
4. 推送到分支
5. 创建 Pull Request

## 许可证

MIT License

## 联系方式

如有问题或建议，请创建 Issue 或联系开发者。

---

**注意**: 使用前请确保已正确配置OpenAI API密钥，并遵守相关API使用条款。
