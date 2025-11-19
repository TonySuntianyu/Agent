# DeepSeek API 设置指南

## 🆓 获取免费DeepSeek API密钥

### 1. 注册DeepSeek账户
1. 访问 [DeepSeek Platform](https://platform.deepseek.com/)
2. 点击"注册"创建免费账户
3. 完成邮箱验证

### 2. 获取API密钥
1. 登录后进入 [API Keys页面](https://platform.deepseek.com/api_keys)
2. 点击"Create API Key"
3. 复制生成的API密钥（格式：`sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`）

### 3. 设置API密钥

**方法1：修改配置文件**
编辑 `config.py` 文件，将第7行的密钥替换为您的真实密钥：
```python
DEEPSEEK_API_KEY = "sk-your_real_deepseek_api_key_here"
```

**方法2：设置环境变量**
```bash
# Windows PowerShell
$env:DEEPSEEK_API_KEY="sk-your_real_deepseek_api_key_here"

# Windows CMD
set DEEPSEEK_API_KEY=sk-your_real_deepseek_api_key_here
```

### 4. 运行项目
```bash
python start_agent.py
```

## 💰 DeepSeek免费额度
- **免费额度**: 每月100万tokens
- **模型**: deepseek-chat (免费)
- **速度**: 快速响应
- **中文支持**: 优秀

## 🔧 故障排除

### 常见问题
1. **API密钥错误**: 检查密钥是否正确复制
2. **网络问题**: 确保能访问 https://api.deepseek.com
3. **额度用完**: 等待下月重置或升级账户

### 测试连接
```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com/v1"
)

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[{"role": "user", "content": "Hello"}]
)
print(response.choices[0].message.content)
```

## 📞 支持
如有问题，请访问 [DeepSeek文档](https://platform.deepseek.com/docs) 或联系技术支持。
