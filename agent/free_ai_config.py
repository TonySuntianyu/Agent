"""
免费AI API配置选择器
"""
import os

# 选择要使用的免费API
API_PROVIDER = "groq"  # 可选: "groq", "deepseek", "ollama", "mock"

if API_PROVIDER == "groq":
    # Groq配置 - 完全免费，速度快
    os.environ["OPENAI_API_KEY"] = "gsk_your_groq_api_key_here"  # 从 https://console.groq.com/ 获取
    os.environ["OPENAI_BASE_URL"] = "https://api.groq.com/openai/v1"
    os.environ["AGENT_MODEL"] = "llama3-8b-8192"
    print("✅ 使用Groq免费API")
    
elif API_PROVIDER == "deepseek":
    # DeepSeek配置
    os.environ["OPENAI_API_KEY"] = "sk-5f7b46dc46d249329debadeecc17996e"
    os.environ["OPENAI_BASE_URL"] = "https://api.deepseek.com/v1"
    os.environ["AGENT_MODEL"] = "deepseek-chat"
    print("✅ 使用DeepSeek API")
    
elif API_PROVIDER == "ollama":
    # Ollama本地配置 - 完全免费
    os.environ["OPENAI_API_KEY"] = "ollama"
    os.environ["OPENAI_BASE_URL"] = "http://localhost:11434"
    os.environ["AGENT_MODEL"] = "llama3.2"
    print("✅ 使用Ollama本地API")
    
elif API_PROVIDER == "mock":
    # 模拟模式 - 完全离线
    os.environ["OPENAI_API_KEY"] = "mock"
    os.environ["AGENT_MODEL"] = "mock"
    print("✅ 使用模拟模式（离线）")


