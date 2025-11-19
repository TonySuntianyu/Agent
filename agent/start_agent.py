"""
图书推荐Agent启动脚本
"""
import os
import sys

# 设置DeepSeek API密钥和模型
os.environ["OPENAI_API_KEY"] = "sk-5f7b46dc46d249329debadeecc17996e"
os.environ["AGENT_MODEL"] = "deepseek-chat"
os.environ["OPENAI_BASE_URL"] = "https://api.deepseek.com/v1"

print("📚 图书推荐Agent启动中...")
print("="*60)

try:
    # 导入必要的模块
    from book_agent import BookRecommendationAgent
    
    print("✅ Agent初始化成功!")
    print("\n🎉 欢迎使用图书推荐Agent!")
    print("="*60)
    print("📖 我可以帮助您：")
    print("   • 搜索图书信息")
    print("   • 基于您浏览的图书推荐相似图书")
    print("   • 根据您的阅读偏好推荐图书")
    print("   • 分析您的阅读趋势")
    print("   • 提供个性化的图书推荐")
    print("="*60)
    print("💬 使用示例：")
    print("   • '搜索《三体》'")
    print("   • '我看了《活着》，推荐相似图书'")
    print("   • '推荐科幻小说'")
    print("   • '分析我的阅读偏好'")
    print("="*60)
    print("❌ 输入 'quit' 或 'exit' 退出")
    print("="*60 + "\n")
    
    # 创建Agent实例
    agent = BookRecommendationAgent()
    
    # 获取用户ID
    user_id = input("请输入您的用户ID (或按回车使用默认): ").strip() or "default_user"
    print(f"👤 欢迎，用户 {user_id}！\n")
    
    # 交互式循环
    while True:
        try:
            user_input = input("您: ").strip()
            
            if user_input.lower() in ['quit', 'exit', '退出']:
                print("👋 再见！")
                break
            
            if not user_input:
                continue
            
            print("🤔 分析中...")
            response = agent.chat(user_input, user_id)
            print(f"📚 图书助手: {response}\n")
            
        except KeyboardInterrupt:
            print("\n👋 再见！")
            break
        except Exception as e:
            print(f"❌ 错误: {e}")
            print("请重试或输入 'quit' 退出\n")

except ImportError as e:
    print(f"❌ 导入错误: {e}")
    print("请确保所有依赖包已正确安装")
    print("运行: pip install -r requirements.txt")
except Exception as e:
    print(f"❌ 运行错误: {e}")
    print("请检查项目文件是否完整")
    import traceback
    traceback.print_exc()
