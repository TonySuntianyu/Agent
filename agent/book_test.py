"""
图书推荐Agent测试文件
"""
import unittest
import json
from unittest.mock import patch, MagicMock
from book_agent import BookRecommendationAgent
from book_tools import BookRecommendationTool, BookSearchTool, BookAnalysisTool
from book_state import BookInfo, UserPreference


class TestBookTools(unittest.TestCase):
    """图书工具测试类"""
    
    def setUp(self):
        """测试前准备"""
        self.recommendation_tool = BookRecommendationTool()
        self.search_tool = BookSearchTool()
        self.analysis_tool = BookAnalysisTool()
    
    def test_search_books(self):
        """测试图书搜索"""
        result = self.search_tool.search_books("刘慈欣", 5)
        self.assertTrue(result["success"])
        self.assertGreater(len(result["results"]), 0)
        
        # 检查搜索结果
        for book in result["results"]:
            self.assertIn("刘慈欣", book["author"])
    
    def test_get_book_details(self):
        """测试获取图书详情"""
        result = self.search_tool.get_book_details("三体")
        self.assertTrue(result["success"])
        self.assertEqual(result["book"]["title"], "三体")
        self.assertEqual(result["book"]["author"], "刘慈欣")
    
    def test_recommend_by_author(self):
        """测试基于作者的推荐"""
        result = self.recommendation_tool.recommend_by_author("刘慈欣", ["三体"])
        self.assertTrue(result["success"])
        self.assertGreater(len(result["recommendations"]), 0)
        
        # 检查推荐结果不包含排除的图书
        titles = [book["title"] for book in result["recommendations"]]
        self.assertNotIn("三体", titles)
    
    def test_recommend_by_genre(self):
        """测试基于类型的推荐"""
        result = self.recommendation_tool.recommend_by_genre("科幻", ["三体"])
        self.assertTrue(result["success"])
        self.assertGreater(len(result["recommendations"]), 0)
        
        # 检查推荐结果都是科幻类型
        for book in result["recommendations"]:
            self.assertEqual(book["genre"], "科幻")
    
    def test_recommend_by_knowledge_graph(self):
        """测试基于知识图谱的推荐"""
        book_info = {
            "title": "三体",
            "author": "刘慈欣",
            "genre": "科幻"
        }
        
        result = self.recommendation_tool.recommend_by_knowledge_graph(book_info)
        self.assertTrue(result["success"])
        self.assertGreater(len(result["recommendations"]), 0)
        self.assertGreater(len(result["reasons"]), 0)
    
    def test_analyze_reading_trends(self):
        """测试阅读趋势分析"""
        user_history = [
            {"title": "三体", "author": "刘慈欣", "genre": "科幻"},
            {"title": "流浪地球", "author": "刘慈欣", "genre": "科幻"},
            {"title": "活着", "author": "余华", "genre": "文学"}
        ]
        
        result = self.analysis_tool.analyze_reading_trends(user_history)
        self.assertTrue(result["success"])
        self.assertEqual(result["analysis"]["total_books"], 3)
        self.assertEqual(result["analysis"]["favorite_genre"], "科幻")
        self.assertEqual(result["analysis"]["favorite_author"], "刘慈欣")
    
    def test_get_similar_books(self):
        """测试获取相似图书"""
        book_info = {
            "title": "三体",
            "author": "刘慈欣",
            "genre": "科幻"
        }
        
        result = self.analysis_tool.get_similar_books(book_info)
        self.assertTrue(result["success"])
        self.assertGreater(len(result["similar_books"]), 0)
        
        # 检查相似度分数
        for similar in result["similar_books"]:
            self.assertIn("similarity_score", similar)
            self.assertIn("similarity_reason", similar)


class TestBookAgent(unittest.TestCase):
    """图书推荐Agent测试类"""
    
    @patch('book_agent.OPENAI_API_KEY', 'test_key')
    @patch('book_agent.llm_with_tools')
    def test_agent_initialization(self, mock_llm):
        """测试Agent初始化"""
        mock_response = MagicMock()
        mock_response.content = "测试响应"
        mock_llm.invoke.return_value = mock_response
        
        agent = BookRecommendationAgent()
        self.assertIsNotNone(agent.graph)
    
    def test_book_info_model(self):
        """测试图书信息模型"""
        book = BookInfo(
            title="三体",
            author="刘慈欣",
            isbn="9787536692930",
            genre="科幻",
            rating=9.0,
            description="地球文明向宇宙发出第一声啼鸣",
            publication_year=2006,
            publisher="重庆出版社"
        )
        
        self.assertEqual(book.title, "三体")
        self.assertEqual(book.author, "刘慈欣")
        self.assertEqual(book.genre, "科幻")
        self.assertEqual(book.rating, 9.0)
    
    def test_user_preference_model(self):
        """测试用户偏好模型"""
        preference = UserPreference(
            favorite_genres=["科幻", "文学"],
            favorite_authors=["刘慈欣", "余华"],
            reading_history=[],
            preferred_rating=8.5
        )
        
        self.assertEqual(preference.favorite_genres, ["科幻", "文学"])
        self.assertEqual(preference.favorite_authors, ["刘慈欣", "余华"])
        self.assertEqual(preference.preferred_rating, 8.5)


class TestBookAgentIntegration(unittest.TestCase):
    """图书推荐Agent集成测试"""
    
    @patch('book_agent.OPENAI_API_KEY', 'test_key')
    def test_agent_with_mock_llm(self):
        """使用模拟LLM测试Agent"""
        from unittest.mock import patch, MagicMock
        from langchain_core.messages import AIMessage
        
        mock_ai_message = AIMessage(content="推荐《流浪地球》和《球状闪电》")
        
        with patch('book_agent.llm_with_tools') as mock_llm:
            mock_llm.invoke.return_value = mock_ai_message
            
            agent = BookRecommendationAgent()
            result = agent.chat("推荐科幻小说")
            
            self.assertEqual(result, "推荐《流浪地球》和《球状闪电》")
    
    def test_recommend_books_method(self):
        """测试推荐图书方法"""
        with patch('book_agent.OPENAI_API_KEY', 'test_key'):
            with patch('book_agent.llm_with_tools') as mock_llm:
                mock_ai_message = MagicMock()
                mock_ai_message.content = "基于《三体》推荐《流浪地球》"
                mock_llm.invoke.return_value = mock_ai_message
                
                agent = BookRecommendationAgent()
                result = agent.recommend_books("三体", "user001")
                
                self.assertIn("user_input", result)
                self.assertEqual(result["user_id"], "user001")


def run_book_tests():
    """运行图书推荐测试"""
    print("运行图书推荐Agent测试...")
    
    # 创建测试套件
    test_suite = unittest.TestSuite()
    
    # 添加测试用例
    test_suite.addTest(unittest.makeSuite(TestBookTools))
    test_suite.addTest(unittest.makeSuite(TestBookAgent))
    test_suite.addTest(unittest.makeSuite(TestBookAgentIntegration))
    
    # 运行测试
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(test_suite)
    
    # 输出结果
    if result.wasSuccessful():
        print("\n✅ 所有图书推荐测试通过！")
    else:
        print(f"\n❌ 测试失败: {len(result.failures)} 个失败, {len(result.errors)} 个错误")
    
    return result.wasSuccessful()


if __name__ == "__main__":
    run_book_tests()
