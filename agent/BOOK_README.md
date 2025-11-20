# 图书推荐Agent

基于LangGraph框架构建的智能图书推荐系统，能够根据用户的阅读历史和偏好，提供个性化的图书推荐服务。

## 🌟 核心功能

### 📚 图书搜索与推荐
- **智能搜索**: 支持按书名、作者、类型等维度搜索图书
- **相似推荐**: 基于用户浏览的图书推荐相似作品
- **知识图谱推荐**: 利用图书知识图谱进行智能推荐
- **个性化推荐**: 根据用户阅读偏好提供定制化推荐
- **扩展书库**: 内置 100+ 本跨语种经典图书，覆盖 30+ 作者 & 10+ 类型

### 🧠 智能分析
- **阅读趋势分析**: 分析用户的阅读习惯和偏好
- **用户画像构建**: 基于阅读历史构建用户画像
- **推荐理由解释**: 为每个推荐提供详细的理由说明

### 🔧 技术特性
- **LangGraph工作流**: 使用LangGraph实现复杂的推荐逻辑
- **多工具集成**: 集成搜索、推荐、分析等多种工具
- **状态管理**: 完整的用户状态和推荐历史跟踪
- **错误处理**: 完善的异常处理和恢复机制
- **本地持久化**: 浏览器自动保存会话列表，可重命名/删除

## 🆕 最近更新（2025.11）

- 📚 图书数据库扩充至 100+ 本，新增古典文学、哲学、心理学等维度
- 🧠 知识图谱新增 20+ 位作者和跨类型关联，支持跨学科推荐
- 💬 Web 前端新增多会话列表、重命名、删除与欢迎提示
- ⏳ 聊天期间展示“正在生成中”动态，输入框与按钮自动锁定
- 🎨 布局改为 95vw 宽度 + 渐变主题 + 新排版规则，阅读体验更佳

## 💻 Web 前端亮点

- **会话列表**：支持多会话、新建、重命名、删除，且自动保存到 localStorage
- **欢迎提示**：页面加载即调用 `/welcome` 接口，展示使用指南
- **状态指示**：LLM 处理中展示动态打字指示器，避免多次提交
- **富文本排版**：自动识别 emoji 标题与列表，控制行距，减少空行
- **可视化体验**：全屏渐变背景、卡片阴影、动画按钮、输入聚焦高亮

## 📁 项目结构

```
codes/
├── book_agent.py           # 图书推荐Agent核心实现
├── book_state.py           # 图书推荐状态定义
├── book_tools.py           # 图书相关工具集合
├── book_example.py         # 使用示例
├── book_test.py            # 测试文件
├── book_run.py             # 快速启动脚本
└── BOOK_README.md          # 图书推荐文档
```

## 🚀 快速开始

### 1. 环境准备

```bash
# 安装依赖
pip install -r requirements.txt

# 设置环境变量
export OPENAI_API_KEY=your_openai_api_key_here
```

### 2. 运行图书推荐Agent

```bash
# 交互式模式
python book_run.py

# 演示模式
python book_run.py demo

# 运行示例
python book_example.py

# 运行测试
python book_test.py
```

## 💡 使用示例

### 基本使用

```python
from book_agent import BookRecommendationAgent

# 创建Agent实例
agent = BookRecommendationAgent()

# 搜索图书
response = agent.chat("搜索刘慈欣的科幻小说")

# 基于图书推荐
result = agent.recommend_books("三体", "user001")

# 搜索并推荐
result = agent.search_and_recommend("余华", "user002")
```

### 交互式使用

```python
# 启动交互式聊天
python book_run.py

# 示例对话：
# 您: 搜索《三体》
# Agent: 找到了《三体》的详细信息...
# 
# 您: 我看了《三体》，推荐相似图书
# Agent: 基于《三体》，我推荐以下图书...
```

## 🛠️ 核心组件

### BookRecommendationState
图书推荐Agent的状态管理，包含：
- 用户信息和偏好
- 当前浏览的图书
- 推荐结果和原因
- 知识图谱数据
- 搜索历史

### 图书工具集合

#### 1. BookSearchTool
- `search_books()`: 搜索图书
- `get_book_details()`: 获取图书详细信息

#### 2. BookRecommendationTool
- `recommend_by_author()`: 基于作者推荐
- `recommend_by_genre()`: 基于类型推荐
- `recommend_by_knowledge_graph()`: 基于知识图谱推荐

#### 3. BookAnalysisTool
- `analyze_reading_trends()`: 分析阅读趋势
- `get_similar_books()`: 获取相似图书

### 知识图谱

系统内置了图书知识图谱，包含：
- **作者关系**: 作者与作品、风格的关系
- **类型关系**: 图书类型之间的相似性
- **推荐路径**: 基于多种因素的推荐路径

## 📊 推荐算法

### 1. 基于作者的推荐
```python
# 推荐同作者的其他作品
recommendations = recommend_by_author("刘慈欣", exclude_books=["三体"])
```

### 2. 基于类型的推荐
```python
# 推荐同类型的其他图书
recommendations = recommend_by_genre("科幻", exclude_books=["三体"])
```

### 3. 基于知识图谱的推荐
```python
# 利用知识图谱进行智能推荐
book_info = {"title": "三体", "author": "刘慈欣", "genre": "科幻"}
recommendations = recommend_by_knowledge_graph(book_info)
```

## 🎯 推荐场景

### 场景1: 用户浏览图书后推荐
```
用户: 我浏览了《三体》
Agent: 基于《三体》，我推荐以下图书：
       1. 《流浪地球》- 刘慈欣 (同作者)
       2. 《球状闪电》- 刘慈欣 (同作者)
       3. 《1984》- 乔治·奥威尔 (相似类型)
```

### 场景2: 基于用户偏好推荐
```
用户: 推荐科幻小说
Agent: 根据您的偏好，推荐以下科幻小说：
       1. 《三体》- 刘慈欣
       2. 《流浪地球》- 刘慈欣
       3. 《球状闪电》- 刘慈欣
```

### 场景3: 搜索并推荐
```
用户: 搜索余华的作品
Agent: 找到余华的作品：
       1. 《活着》- 余华
       2. 《许三观卖血记》- 余华
       基于这些作品，我还推荐：
       3. 《百年孤独》- 加西亚·马尔克斯 (相似风格)
```

## 🔧 配置选项

### 模型配置
```python
# 在config.py中修改
AGENT_MODEL = "gpt-4"          # 模型名称
TEMPERATURE = 0.7              # 温度参数
MAX_ITERATIONS = 5             # 最大迭代次数
```

### 图书数据库

当前版本内置 100+ 本图书，覆盖：

- **类型**：科幻、反乌托邦、魔幻现实主义、推理、古典文学、现代文学、散文、戏剧、哲学、心理学、历史、科普等
- **作者**：刘慈欣、东野圭吾、村上春树、加西亚·马尔克斯、鲁迅、曹雪芹、尼采、霍金、赫拉利等 30+ 位
- **特点**：为每本书标注 ISBN、评分、年份、出版社与简介，并在知识图谱中维护作者-风格-类型映射
```python
# 在book_tools.py中添加图书数据
books = [
    {
        "title": "图书标题",
        "author": "作者",
        "genre": "类型",
        "rating": 评分,
        "description": "描述"
    }
]
```

## 📈 扩展功能

### 1. 添加新的推荐算法
```python
def custom_recommendation_algorithm(book_info):
    # 实现自定义推荐逻辑
    pass
```

### 2. 集成外部API
```python
def integrate_external_book_api():
    # 集成外部图书API
    pass
```

### 3. 用户行为分析
```python
def analyze_user_behavior(user_history):
    # 分析用户行为模式
    pass
```

## 🧪 测试

### 运行测试
```bash
python book_test.py
```

### 测试覆盖
- 图书搜索功能
- 推荐算法
- 知识图谱
- 用户偏好分析
- Agent集成测试

## 🚨 故障排除

### 常见问题

1. **API密钥错误**
   ```
   错误: 请设置OPENAI_API_KEY环境变量
   解决: 检查环境变量设置
   ```

2. **图书数据缺失**
   ```
   错误: 未找到图书
   解决: 检查book_tools.py中的图书数据
   ```

3. **推荐结果为空**
   ```
   错误: 没有找到推荐图书
   解决: 检查知识图谱配置和推荐算法
   ```

## 🔮 未来规划

- [ ] 集成真实图书数据库API
- [ ] 添加用户评分和评论功能
- [ ] 实现协同过滤推荐
- [ ] 添加图书封面和详细信息
- [ ] 支持多语言图书推荐
- [ ] 添加阅读进度跟踪

## 📞 支持

如有问题或建议，请创建Issue或联系开发团队。

---

**注意**: 使用前请确保已正确配置OpenAI API密钥，并遵守相关API使用条款。
