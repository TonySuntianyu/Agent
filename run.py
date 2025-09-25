"""
快速启动脚本
"""
import os
import sys
from agent import LangGraphAgent


def main():
    """主函数"""
    print("🚀 LangGraph Agent 启动中...")
    
    # 检查环境变量
    if not os.getenv("OPENAI_API_KEY"):
        print("❌ 错误: 请设置OPENAI_API_KEY环境变量")
        print("💡 提示: 您可以在.env文件中设置，或者直接设置环境变量")
        print("   例如: export OPENAI_API_KEY=your_api_key_here")
        return
    
    try:
        # 创建Agent实例
        print("🤖 初始化Agent...")
        agent = LangGraphAgent()
        print("✅ Agent初始化成功!")
        
        # 显示欢迎信息
        print("\n" + "="*50)
        print("🎉 欢迎使用 LangGraph Agent!")
        print("="*50)
        print("💬 您可以问我任何问题，我会使用合适的工具来帮助您")
        print("🛠️  支持的功能: 计算、文件操作、数据分析、时间查询等")
        print("❌ 输入 'quit' 或 'exit' 退出")
        print("="*50 + "\n")
        
        # 交互式循环
        while True:
            try:
                user_input = input("您: ").strip()
                
                if user_input.lower() in ['quit', 'exit', '退出']:
                    print("👋 再见！")
                    break
                
                if not user_input:
                    continue
                
                print("🤔 思考中...")
                response = agent.chat(user_input)
                print(f"🤖 Agent: {response}\n")
                
            except KeyboardInterrupt:
                print("\n👋 再见！")
                break
            except Exception as e:
                print(f"❌ 错误: {e}")
                print("请重试或输入 'quit' 退出\n")
    
    except Exception as e:
        print(f"❌ 初始化失败: {e}")
        print("请检查配置和依赖是否正确安装")


if __name__ == "__main__":
    main()
