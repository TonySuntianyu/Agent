"""
Gemini API 测试脚本
"""
import os

from google import genai


def main() -> None:
    """调用 Gemini 生成式内容接口，验证 API 是否可用"""
    # 确保已设置 GEMINI_API_KEY 环境变量
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise EnvironmentError("请先设置 GEMINI_API_KEY 环境变量")

    client = genai.Client(api_key=api_key)

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents="1 + 12 是多少？",
        )
        print("API 成功响应:", response.text)
    except Exception as exc:
        print(f"API 调用失败: {exc}")


if __name__ == "__main__":
    main()

