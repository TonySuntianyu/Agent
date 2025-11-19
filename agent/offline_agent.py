"""
离线图书推荐Agent - 不依赖任何AI API
"""
import json
import random
from book_tools import book_search_tool, book_recommendation_tool, book_analysis_tool

class OfflineBookAgent:
    """离线图书推荐Agent"""
    
    def __init__(self):
        self.search_tool = book_search_tool
        self.recommendation_tool = book_recommendation_tool
        self.analysis_tool = book_analysis_tool
    
    def chat(self, message: str, user_id: str = None) -> str:
        """离线聊天接口"""
        message_lower = message.lower()
        
        # 搜索图书
        if "搜索" in message or "查找" in message:
            # 提取搜索关键词
            query = message.replace("搜索", "").replace("查找", "").replace("《", "").replace("》", "").strip()
            result = self.search_tool.search_books(query, 5)
            
            if result["success"] and result["results"]:
                response = f"找到以下图书：\n"
                for i, book in enumerate(result["results"], 1):
                    response += f"{i}. 《{book['title']}》- {book['author']} ({book['genre']})\n"
                    response += f"   评分: {book['rating']}/10\n"
                    response += f"   描述: {book['description']}\n\n"
                return response
            else:
                return "抱歉，没有找到相关图书。"
        
        # 推荐相似图书
        elif "推荐" in message and "相似" in message:
            # 提取图书名称
            book_title = message.replace("推荐", "").replace("相似", "").replace("《", "").replace("》", "").strip()
            book_info = {"title": book_title, "author": "", "genre": ""}
            
            # 先搜索这本书
            search_result = self.search_tool.get_book_details(book_title)
            if search_result["success"]:
                book_info = search_result["book"]
                result = self.recommendation_tool.recommend_by_knowledge_graph(book_info)
                
                if result["success"] and result["recommendations"]:
                    response = f"基于《{book_title}》，我推荐以下图书：\n"
                    for i, book in enumerate(result["recommendations"], 1):
                        response += f"{i}. 《{book['title']}》- {book['author']} ({book['genre']})\n"
                        response += f"   评分: {book['rating']}/10\n"
                        response += f"   推荐理由: {result['reasons'][i-1] if i <= len(result['reasons']) else '相似类型'}\n\n"
                    return response
                else:
                    return "抱歉，无法找到相似图书。"
            else:
                return f"抱歉，没有找到图书《{book_title}》。"
        
        # 类型推荐
        elif "推荐" in message and ("类型" in message or "类型" in message):
            # 提取类型
            genre = message.replace("推荐", "").replace("类型", "").replace("的", "").strip()
            result = self.recommendation_tool.recommend_by_genre(genre)
            
            if result["success"] and result["recommendations"]:
                response = f"推荐{genre}类型的图书：\n"
                for i, book in enumerate(result["recommendations"], 1):
                    response += f"{i}. 《{book['title']}》- {book['author']}\n"
                    response += f"   评分: {book['rating']}/10\n"
                    response += f"   描述: {book['description']}\n\n"
                return response
            else:
                return f"抱歉，没有找到{genre}类型的图书。"
        
        # 获取图书详情
        elif "详情" in message or "信息" in message:
            # 提取图书名称
            book_title = message.replace("详情", "").replace("信息", "").replace("《", "").replace("》", "").strip()
            result = self.search_tool.get_book_details(book_title)
            
            if result["success"]:
                book = result["book"]
                response = f"《{book['title']}》详细信息：\n"
                response += f"作者: {book['author']}\n"
                response += f"类型: {book['genre']}\n"
                response += f"评分: {book['rating']}/10\n"
                response += f"出版年份: {book['publication_year']}\n"
                response += f"出版社: {book['publisher']}\n"
                response += f"ISBN: {book['isbn']}\n"
                response += f"描述: {book['description']}\n"
                return response
            else:
                return f"抱歉，没有找到图书《{book_title}》。"
        
        # 默认回复
        else:
            return "我是图书推荐助手，可以帮您：\n1. 搜索图书：'搜索《书名》'\n2. 推荐相似图书：'推荐《书名》的相似图书'\n3. 类型推荐：'推荐科幻类型图书'\n4. 查看详情：'《书名》的详细信息'"

def main():
    """主函数"""
    print("📚 离线图书推荐Agent启动中...")
    print("="*60)
    print("🎉 欢迎使用离线图书推荐Agent!")
    print("="*60)
    print("📖 我可以帮助您：")
    print("   • 搜索图书信息")
    print("   • 基于您浏览的图书推荐相似图书")
    print("   • 根据图书类型推荐图书")
    print("   • 查看图书详细信息")
    print("="*60)
    print("💬 使用示例：")
    print("   • '搜索《三体》'")
    print("   • '推荐《三体》的相似图书'")
    print("   • '推荐科幻类型图书'")
    print("   • '《三体》的详细信息'")
    print("="*60)
    print("❌ 输入 'quit' 或 'exit' 退出")
    print("="*60 + "\n")
    
    # 创建Agent实例
    agent = OfflineBookAgent()
    
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

if __name__ == "__main__":
    main()


