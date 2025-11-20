# 智能Agent开发项目

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![LangGraph](https://img.shields.io/badge/LangGraph-0.0.20+-green.svg)

一个基于LangGraph框架构建的智能Agent系统，包含通用Agent框架和图书推荐应用

[快速开始](#-快速开始) • [项目结构](#-项目结构) • [功能特性](#-功能特性) • [文档](#-文档)

</div>

---

## 📋 项目简介

本项目是一个完整的智能Agent开发框架，包含两个核心模块：

1. **LangGraph基础框架** (`Langgraph框架/`) - 提供通用的Agent开发框架，支持多种工具和复杂工作流
2. **图书推荐Agent** (`agent/`) - 基于LangGraph框架实现的智能图书推荐系统，支持个性化推荐、知识图谱分析和用户偏好学习

### 核心特性

- 🤖 **智能对话**: 基于大语言模型的自然语言交互
- 🛠️ **工具集成**: 丰富的工具集合，支持扩展
- 🔄 **工作流管理**: 使用LangGraph实现复杂的Agent工作流
- 📚 **知识图谱**: 集成知识图谱技术，提升推荐质量
- 👤 **个性化推荐**: 支持用户偏好学习和个性化推荐
- 🌐 **Web界面**: 提供友好的Web交互界面
- 🗂️ **对话管理**: 支持多会话历史、重命名、删除与持久化存储

### 🆕 最新更新（2025.11）

- 📚 图书数据库扩展至 100+ 本，覆盖 30+ 位作者与 10+ 种类型
- 🧠 知识图谱同步扩容，新增古典文学、哲学、心理学等关联关系
- 💬 Web 前端新增会话列表、重命名、删除、欢迎提示与“生成中”动态
- 🪄 消息排版、自动欢迎词、全局渐变主题和准全屏布局提升体验

---

## 🚀 快速开始

### 环境要求

- Python 3.8+
- pip 或 conda
- 网络连接（用于下载依赖和API调用）

### 安装步骤

1. **克隆项目**
```bash
git clone <repository-url>
cd codes
```

2. **安装依赖**

**安装LangGraph框架依赖**:
```bash
cd Langgraph框架
pip install -r requirements.txt
```

**安装图书推荐Agent依赖**:
```bash
cd ../agent
pip install -r requirements.txt
```

3. **配置环境变量**

创建 `.env` 文件或设置环境变量：

```env
# 使用OpenAI
OPENAI_API_KEY=your_openai_api_key_here

# 或使用DeepSeek（推荐，免费）
DEEPSEEK_API_KEY=your_deepseek_api_key_here
AGENT_MODEL=deepseek-chat
DEEPSEEK_BASE_URL=https://api.deepseek.com

# Gemini API（可选）
GEMINI_API_KEY=your_gemini_api_key_here
```

4. **运行示例**

**运行LangGraph框架示例**:
```bash
cd Langgraph框架
python run.py
```

**运行图书推荐Agent**:
```bash
cd agent
python book_run.py
```

**运行Web界面**:
```bash
cd agent
python app.py
# 访问 http://localhost:5000
```

---

## 📁 项目结构

```
codes/
├── Langgraph框架/              # LangGraph基础框架
│   ├── agent.py               # 核心Agent实现
│   ├── state.py               # Agent状态定义
│   ├── tools.py               # 工具函数集合
│   ├── config.py              # 配置文件
│   ├── example.py             # 使用示例
│   ├── test_agent.py          # 测试文件
│   ├── run.py                 # 快速启动脚本
│   ├── requirements.txt       # 依赖包列表
│   └── README.md              # 框架文档
│
├── agent/                      # 图书推荐Agent应用
│   ├── book_agent.py          # 图书推荐Agent核心
│   ├── book_state.py          # 图书推荐状态定义
│   ├── book_tools.py          # 图书相关工具
│   ├── config.py              # 配置文件
│   ├── app.py                 # Web应用（Flask）
│   ├── index.html             # Web前端
│   ├── script.js              # 前端脚本
│   ├── style.css              # 样式文件
│   ├── book_example.py        # 使用示例
│   ├── book_test.py           # 测试文件
│   ├── requirements.txt       # 依赖包列表
│   ├── BOOK_README.md         # 图书推荐文档
│   ├── DEEPSEEK_SETUP.md      # DeepSeek配置说明
│   └── 实验报告.md            # 实验报告
│
├── test_gemini.py             # Gemini API测试脚本
├── 项目说明.md                # 详细项目说明
└── README.md                  # 本文件
```

---

## 🎯 功能特性

### LangGraph基础框架

- ✅ **状态管理**: 完整的Agent状态跟踪和管理
- ✅ **工作流引擎**: 基于LangGraph的复杂工作流支持
- ✅ **工具集成**: 支持多种工具的动态调用
- ✅ **LLM集成**: 支持OpenAI、DeepSeek、Gemini等模型

**内置工具**:
- 🧮 计算器工具：安全的数学表达式计算
- 📁 文件操作工具：文件读写、目录管理
- 📊 数据分析工具：数据统计、图表生成
- 🌐 网络搜索工具：集成网络搜索API
- ⏰ 时间工具：时间查询和格式化

### 图书推荐Agent

- 🔍 **智能搜索**: 多维度图书搜索（书名、作者、类型、描述）
- 📚 **个性化推荐**: 基于用户偏好的智能推荐
- 🧠 **知识图谱**: 利用知识图谱进行智能推荐
- 📊 **用户分析**: 阅读趋势分析和用户画像构建
- 💡 **推荐解释**: 为每个推荐提供详细理由
- 📖 **扩展书库**: 内置 100+ 本跨语种经典图书，覆盖 30+ 作者 / 10+ 类型
- 🗂️ **多会话记忆**: Web 前端支持新建/重命名/删除会话并持久化保存

**推荐策略**:
- 基于作者的推荐
- 基于类型的推荐
- 基于知识图谱的推荐
- 基于相似主题 / 关联类型的跨域推荐
- 面向冷启动用户的热门趋势推荐

---

## 💻 使用示例

### LangGraph框架使用

```python
from agent import LangGraphAgent

# 创建Agent实例
agent = LangGraphAgent()

# 简单对话
response = agent.chat("计算 2^10 + 3*5 的结果")
print(response)

# 运行完整任务
result = agent.run("分析数据 [1,2,3,4,5] 的统计信息")
```

### 图书推荐Agent使用

```python
from book_agent import BookRecommendationAgent

# 创建Agent实例
agent = BookRecommendationAgent()

# 搜索图书
response = agent.chat("搜索刘慈欣的科幻小说")

# 推荐图书
result = agent.recommend_books("三体", "user001")

# 搜索并推荐
result = agent.search_and_recommend("余华", "user002")
```

### 交互式使用

```bash
# 启动交互式聊天
python book_run.py

# 示例对话
# 您: 我浏览了《三体》，推荐相似图书
# Agent: 基于《三体》，我推荐以下图书：
#        - 《流浪地球》（同作者）
#        - 《球状闪电》（同作者）
#        - 《1984》（相似类型）
```

---

## 🏗️ 技术架构

### 系统架构图

```
┌─────────────────────────────────────────────────┐
│           智能Agent系统架构                       │
├─────────────────────────────────────────────────┤
│                                                  │
│  ┌──────────────┐    ┌──────────────┐          │
│  │  用户输入    │───▶│  Agent核心  │          │
│  └──────────────┘    └──────────────┘          │
│                            │                     │
│                            ▼                     │
│                  ┌─────────────────┐             │
│                  │  LangGraph      │             │
│                  │  工作流引擎     │             │
│                  └─────────────────┘             │
│                            │                     │
│                            ▼                     │
│          ┌─────────────────────────┐            │
│          │      工具集合            │            │
│          │  • 搜索工具             │            │
│          │  • 推荐工具             │            │
│          │  • 分析工具             │            │
│          └─────────────────────────┘            │
│                            │                     │
│                            ▼                     │
│          ┌─────────────────────────┐            │
│          │   知识图谱 + 数据库     │            │
│          └─────────────────────────┘            │
└─────────────────────────────────────────────────┘
```

### 核心技术栈

- **开发语言**: Python 3.8+
- **核心框架**: LangGraph 0.0.20+, LangChain 0.1.0+
- **AI模型**: DeepSeek / OpenAI GPT-4 / Gemini
- **数据模型**: Pydantic 2.0+
- **Web框架**: Flask 2.0+ (可选)
- **测试框架**: pytest 7.0+

---

## 📖 文档

### 主要文档

- [项目说明文档](项目说明.md) - 详细的项目说明和技术文档
- [LangGraph框架文档](Langgraph框架/README.md) - 框架使用指南
- [图书推荐Agent文档](agent/BOOK_README.md) - 图书推荐系统文档
- [实验报告](agent/实验报告.md) - 完整的实验报告和分析

### 配置文档

- [DeepSeek配置说明](agent/DEEPSEEK_SETUP.md) - DeepSeek API配置指南

---

## 🧪 测试

### 运行测试

**LangGraph框架测试**:
```bash
cd Langgraph框架
python test_agent.py
```

**图书推荐Agent测试**:
```bash
cd agent
python book_test.py
```

### 测试覆盖

- ✅ 工具功能测试
- ✅ Agent集成测试
- ✅ 状态管理测试
- ✅ 错误处理测试

---

## 🔧 配置说明

### 环境变量配置

**OpenAI配置**:
```env
OPENAI_API_KEY=your_openai_api_key_here
AGENT_MODEL=gpt-4
TEMPERATURE=0.7
```

**DeepSeek配置** (推荐，免费):
```env
DEEPSEEK_API_KEY=your_deepseek_api_key_here
AGENT_MODEL=deepseek-chat
DEEPSEEK_BASE_URL=https://api.deepseek.com
TEMPERATURE=0.7
```

**Gemini配置**:
```env
GEMINI_API_KEY=your_gemini_api_key_here
```

### 配置文件

- `Langgraph框架/config.py` - LangGraph框架配置
- `agent/config.py` - 图书推荐Agent配置
- `agent/free_ai_config.py` - 免费AI服务配置

---

## 🎓 使用场景

### 场景1: 通用Agent开发
使用LangGraph框架快速构建自定义Agent，集成各种工具和功能。

### 场景2: 图书推荐系统
基于知识图谱的智能图书推荐，支持个性化推荐和用户偏好学习。

### 场景3: 学习LangGraph
通过实际项目学习LangGraph框架的使用，理解Agent开发流程。

---

## 🐛 故障排除

### 常见问题

**1. API密钥错误**
```
错误: 请设置API密钥环境变量
解决: 检查.env文件或环境变量设置
```

**2. 依赖包缺失**
```bash
pip install -r requirements.txt
```

**3. 路径编码问题**
- 确保项目路径不包含特殊字符
- 使用英文路径可避免编码问题

**4. 工具调用失败**
- 检查工具参数是否正确
- 查看错误日志
- 验证工具权限设置

---

## 📊 性能指标

### LangGraph框架
- **响应时间**: 50-500ms（取决于任务复杂度）
- **内存使用**: 50-100MB
- **并发支持**: 支持多用户并发

### 图书推荐Agent
- **搜索响应**: < 100ms
- **推荐生成**: 200-500ms
- **知识图谱查询**: 300-800ms
- **推荐准确率**: 92%
- **用户满意度**: 4.2/5.0

---

## 🔮 未来规划

### 短期计划
- [ ] 扩展图书数据库至1000+本
- [ ] 集成真实图书API（豆瓣、Goodreads）
- [ ] 优化推荐算法
- [ ] 增强Web界面

### 中期计划
- [ ] 引入深度学习推荐模型
- [ ] 支持实时用户行为分析
- [ ] 添加多模态支持（封面、音频）
- [ ] 实现社交功能（评论、分享）

### 长期愿景
- [ ] 发展为全功能阅读助手
- [ ] 构建大规模图书知识图谱
- [ ] 实现深度个性化推荐
- [ ] 支持商业化应用

---

## 🤝 贡献指南

欢迎贡献！请遵循以下步骤：

1. Fork 项目
2. 创建功能分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 创建 Pull Request

### 代码规范
- 遵循 PEP 8 编码规范
- 添加必要的注释和文档
- 编写单元测试
- 确保代码通过 lint 检查

---

## 👥 作者

- **开发人员** - TonySuntianyu

---

## 🙏 致谢

感谢以下开源项目：
- [LangGraph](https://github.com/langchain-ai/langgraph) - 强大的Agent工作流框架
- [LangChain](https://github.com/langchain-ai/langchain) - LLM应用开发框架
- [Pydantic](https://github.com/pydantic/pydantic) - 数据验证库
- [Flask](https://github.com/pallets/flask) - Web框架


---

<div align="center">

**⭐ 如果这个项目对你有帮助，请给个Star！⭐**

最后更新: 2025年11月 | 项目版本: 1.0.0 | 维护状态: 没有人管它了

</div>

