"""
图书推荐Agent使用示例
"""
import os
import json
from book_agent import BookRecommendationAgent

# 手动加载 .env 文件
try:
    with open('.env', 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#') and '=' in line:
                key, value = line.split('=', 1)
                key = key.strip()
                value = value.strip()
                if key == 'DEEPSEEK_API_KEY':
                    os.environ[key] = value
except FileNotFoundError:
    pass # .env文件不存在也没关系




def main():
    """主函数"""
    print("=== 图书推荐Agent示例 ===\n")
    
    # 创建Agent实例
    agent = BookRecommendationAgent()
    
    # 示例1: 搜索图书
    print("示例1: 搜索图书")
    print("问题: 搜索刘慈欣的科幻小说")
    result1 = agent.chat("搜索刘慈欣的科幻小说")
    print(f"回答: {result1}\n")
    
    # 示例2: 基于图书推荐
    print("示例2: 基于图书推荐")
    print("问题: 我浏览了《三体》，请推荐相似图书")
    result2 = agent.recommend_books("三体", "user001")
    print(f"推荐结果: {result2.get('recommendations', [])}")
    print(f"推荐原因: {result2.get('recommendation_reasons', [])}\n")
    
    # 示例3: 搜索并推荐
    print("示例3: 搜索并推荐")
    print("问题: 搜索余华的作品，然后推荐相关图书")
    result3 = agent.search_and_recommend("余华", "user002")
    print(f"搜索结果和推荐: {result3}\n")
    
    # 示例4: 基于类型的推荐
    print("示例4: 基于类型的推荐")
    print("问题: 推荐科幻类型的图书")
    result4 = agent.chat("推荐科幻类型的图书")
    print(f"回答: {result4}\n")
    
    # 示例5: 获取图书详细信息
    print("示例5: 获取图书详细信息")
    print("问题: 获取《活着》的详细信息")
    result5 = agent.chat("获取《活着》的详细信息")
    print(f"回答: {result5}\n")


def interactive_book_recommendation():
    """交互式图书推荐"""
    print("=== 交互式图书推荐模式 ===")
    print("输入 'quit' 退出\n")
    
    agent = BookRecommendationAgent()
    user_id = input("请输入您的用户ID (或按回车使用默认): ").strip() or "default_user"
    
    print(f"欢迎，用户 {user_id}！")
    print("您可以：")
    print("1. 搜索图书：'搜索《书名》'")
    print("2. 获取推荐：'我看了《书名》，推荐相似图书'")
    print("3. 浏览推荐：'推荐科幻小说'")
    print("4. 查看详情：'《书名》的详细信息'")
    print("5. 输入 'quit' 退出\n")
    
    while True:
        try:
            user_input = input("您: ").strip()
            if user_input.lower() == 'quit':
                print("再见！")
                break
            
            if not user_input:
                continue
            
            print("🤔 分析中...")
            response = agent.chat(user_input, user_id)
            print(f"📚 图书助手: {response}\n")
            
        except KeyboardInterrupt:
            print("\n再见！")
            break
        except Exception as e:
            print(f"❌ 错误: {e}")
            print("请重试或输入 'quit' 退出\n")


def demonstrate_knowledge_graph():
    """演示知识图谱功能"""
    print("=== 知识图谱推荐演示 ===\n")
    
    agent = BookRecommendationAgent()
    
    # 演示不同图书的推荐
    test_books = ["三体", "活着", "百年孤独", "1984"]
    
    for book in test_books:
        print(f"📖 浏览图书: 《{book}》")
        result = agent.recommend_books(book, "demo_user")
        
        if result.get("recommendations"):
            print("🎯 推荐图书:")
            for i, rec in enumerate(result["recommendations"][:3], 1):
                print(f"  {i}. 《{rec['title']}》 - {rec['author']} ({rec['genre']})")
        
        if result.get("recommendation_reasons"):
            print("💡 推荐理由:")
            for reason in result["recommendation_reasons"]:
                print(f"  - {reason}")
        
        print("-" * 50)


def demonstrate_user_preferences():
    """演示用户偏好分析"""
    print("=== 用户偏好分析演示 ===\n")
    
    agent = BookRecommendationAgent()
    
    # 模拟用户浏览历史
    user_history = [
        {"title": "三体", "author": "刘慈欣", "genre": "科幻"},
        {"title": "流浪地球", "author": "刘慈欣", "genre": "科幻"},
        {"title": "活着", "author": "余华", "genre": "文学"},
        {"title": "百年孤独", "author": "加西亚·马尔克斯", "genre": "魔幻现实主义"}
    ]
    
    print("📊 分析用户阅读历史...")
    history_str = json.dumps(user_history, ensure_ascii=False)
    result = agent.chat(f"分析我的阅读历史: {history_str}")
    print(f"分析结果: {result}\n")
    
    # 基于偏好推荐
    print("🎯 基于偏好推荐...")
    result = agent.chat("基于我的阅读偏好，推荐一些图书")
    print(f"推荐结果: {result}\n")


if __name__ == "__main__":
    # 检查环境变量
    if not os.getenv("DEEPSEEK_API_KEY"):
        print("请设置DEEPSEEK_API_KEY环境变量")
        print("您可以在.env文件中设置，或者直接设置环境变量")
        exit(1)
    
    # 运行示例
    main()
    
    # 演示知识图谱
    demonstrate_knowledge_graph()
    
    # 演示用户偏好
    demonstrate_user_preferences()
    
    # 询问是否进入交互模式
    choice = input("是否进入交互式图书推荐模式？(y/n): ")
    if choice.lower() == 'y':
        interactive_book_recommendation()
