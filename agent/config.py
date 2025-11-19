"""
图书推荐Agent配置文件 - 使用DeepSeek免费API
"""
import os

# DeepSeek配置
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY", "sk-5f7b46dc46d249329debadeecc17996e")
AGENT_MODEL = os.getenv("AGENT_MODEL", "deepseek-chat")
TEMPERATURE = float(os.getenv("TEMPERATURE", "0.7"))
DEEPSEEK_BASE_URL = os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com/v1")

# Agent配置
MAX_ITERATIONS = int(os.getenv("MAX_ITERATIONS", "5"))
DEFAULT_USER_ID = os.getenv("DEFAULT_USER_ID", "default_user")

# 图书推荐配置
RECOMMENDATION_LIMIT = int(os.getenv("RECOMMENDATION_LIMIT", "5"))
SEARCH_LIMIT = int(os.getenv("SEARCH_LIMIT", "10"))

# 知识图谱配置
ENABLE_KNOWLEDGE_GRAPH = os.getenv("ENABLE_KNOWLEDGE_GRAPH", "true").lower() == "true"

# 日志配置
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
ENABLE_DEBUG = os.getenv("ENABLE_DEBUG", "false").lower() == "true"

# 验证配置
if not DEEPSEEK_API_KEY or DEEPSEEK_API_KEY == "sk-your_deepseek_api_key_here":
    print("⚠️  请设置DeepSeek API密钥")
    print("📝 获取免费API密钥: https://platform.deepseek.com/")
    print("🔧 设置方法: export DEEPSEEK_API_KEY=your_deepseek_api_key_here")
    print("💡 或者直接修改config.py中的DEEPSEEK_API_KEY")

