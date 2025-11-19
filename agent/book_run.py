"""
图书推荐Agent快速启动脚本
"""
import os
import sys
from book_agent import BookRecommendationAgent


def main():
    """主函数"""
    print("📚 图书推荐Agent启动中...")
    
    # 检查环境变量
    if not os.getenv("OPENAI_API_KEY"):
        print("❌ 错误: 请设置OPENAI_API_KEY环境变量")
        print("💡 提示: 您可以在.env文件中设置，或者直接设置环境变量")
        print("   例如: export OPENAI_API_KEY=your_api_key_here")
        return
    
    try:
        # 创建Agent实例
        print("🤖 初始化图书推荐Agent...")
        agent = BookRecommendationAgent()
        print("✅ Agent初始化成功!")
        
        # 显示欢迎信息
        print("\n" + "="*60)
        print("🎉 欢迎使用图书推荐Agent!")
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
    
    except Exception as e:
        print(f"❌ 初始化失败: {e}")
        print("请检查配置和依赖是否正确安装")


def demo_mode():
    """演示模式"""
    print("🎬 图书推荐Agent演示模式")
    print("="*50)
    
    agent = BookRecommendationAgent()
    
    # 演示场景
    demo_scenarios = [
        {
            "title": "场景1: 搜索图书",
            "input": "搜索刘慈欣的科幻小说",
            "description": "演示如何搜索特定作者的图书"
        },
        {
            "title": "场景2: 基于图书推荐",
            "input": "我浏览了《三体》，请推荐相似图书",
            "description": "演示如何基于用户浏览的图书进行推荐"
        },
        {
            "title": "场景3: 类型推荐",
            "input": "推荐科幻类型的图书",
            "description": "演示如何根据图书类型进行推荐"
        },
        {
            "title": "场景4: 获取图书详情",
            "input": "获取《活着》的详细信息",
            "description": "演示如何获取图书的详细信息"
        }
    ]
    
    for i, scenario in enumerate(demo_scenarios, 1):
        print(f"\n{scenario['title']}")
        print(f"描述: {scenario['description']}")
        print(f"输入: {scenario['input']}")
        print("🤔 处理中...")
        
        try:
            response = agent.chat(scenario['input'], f"demo_user_{i}")
            print(f"📚 回答: {response}")
        except Exception as e:
            print(f"❌ 错误: {e}")
        
        print("-" * 50)
        
        # 询问是否继续
        if i < len(demo_scenarios):
            continue_demo = input("按回车继续下一个演示，或输入 'q' 退出: ").strip()
            if continue_demo.lower() == 'q':
                break
    
    print("\n🎉 演示完成！")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "demo":
        demo_mode()
    else:
        main()
