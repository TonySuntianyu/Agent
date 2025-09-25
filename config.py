"""
配置文件
"""
import os
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

# OpenAI配置
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
AGENT_MODEL = os.getenv("AGENT_MODEL", "gpt-4")
TEMPERATURE = float(os.getenv("TEMPERATURE", "0.7"))
MAX_ITERATIONS = int(os.getenv("MAX_ITERATIONS", "10"))

# 其他API配置
SERPER_API_KEY = os.getenv("SERPER_API_KEY")
WOLFRAM_ALPHA_APPID = os.getenv("WOLFRAM_ALPHA_APPID")

# 验证必要的配置
if not OPENAI_API_KEY:
    raise ValueError("请设置OPENAI_API_KEY环境变量")
