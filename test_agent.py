"""
Agent测试文件
"""
import unittest
import json
from unittest.mock import patch, MagicMock
from agent import LangGraphAgent
from tools import CalculatorTool, TimeTool, FileTool


class TestAgent(unittest.TestCase):
    """Agent测试类"""
    
    def setUp(self):
        """测试前准备"""
        self.agent = LangGraphAgent()
    
    def test_calculator_tool(self):
        """测试计算器工具"""
        calc = CalculatorTool()
        
        # 测试基本计算
        result = calc.calculate("2 + 3")
        self.assertTrue(result["success"])
        self.assertEqual(result["result"], 5)
        
        # 测试复杂计算
        result = calc.calculate("2**10 + 3*5")
        self.assertTrue(result["success"])
        self.assertEqual(result["result"], 1024 + 15)
        
        # 测试错误处理
        result = calc.calculate("invalid_expression")
        self.assertFalse(result["success"])
        self.assertIn("error", result)
    
    def test_time_tool(self):
        """测试时间工具"""
        time_tool = TimeTool()
        
        # 测试获取当前时间
        result = time_tool.get_current_time()
        self.assertTrue(result["success"])
        self.assertIn("current_time", result)
        self.assertIn("timestamp", result)
    
    def test_file_tool(self):
        """测试文件工具"""
        file_tool = FileTool()
        
        # 测试列出文件
        result = file_tool.list_files(".")
        self.assertTrue(result["success"])
        self.assertIn("files", result)
        
        # 测试写入和读取文件
        test_content = "测试内容"
        test_file = "test_file.txt"
        
        # 写入文件
        write_result = file_tool.write_file(test_file, test_content)
        self.assertTrue(write_result["success"])
        
        # 读取文件
        read_result = file_tool.read_file(test_file)
        self.assertTrue(read_result["success"])
        self.assertEqual(read_result["content"], test_content)
        
        # 清理测试文件
        import os
        if os.path.exists(test_file):
            os.remove(test_file)
    
    @patch('agent.OPENAI_API_KEY', 'test_key')
    @patch('agent.llm_with_tools')
    def test_agent_initialization(self, mock_llm):
        """测试Agent初始化"""
        # 模拟LLM响应
        mock_response = MagicMock()
        mock_response.content = "测试响应"
        mock_llm.invoke.return_value = mock_response
        
        agent = LangGraphAgent()
        self.assertIsNotNone(agent.graph)
    
    def test_data_analysis_tool(self):
        """测试数据分析工具"""
        from tools import DataAnalysisTool
        
        data_tool = DataAnalysisTool()
        
        # 测试数据分析
        test_data = [{"value": i} for i in range(1, 6)]
        result = data_tool.analyze_data(test_data)
        
        self.assertTrue(result["success"])
        self.assertIn("statistics", result)
        self.assertIn("value", result["statistics"])


class TestAgentIntegration(unittest.TestCase):
    """Agent集成测试"""
    
    @patch('agent.OPENAI_API_KEY', 'test_key')
    def test_agent_with_mock_llm(self):
        """使用模拟LLM测试Agent"""
        from unittest.mock import patch, MagicMock
        from langchain_core.messages import AIMessage
        
        # 模拟LLM响应
        mock_ai_message = AIMessage(content="这是一个测试响应")
        
        with patch('agent.llm_with_tools') as mock_llm:
            mock_llm.invoke.return_value = mock_ai_message
            
            agent = LangGraphAgent()
            result = agent.chat("测试消息")
            
            self.assertEqual(result, "这是一个测试响应")


def run_tests():
    """运行所有测试"""
    print("运行Agent测试...")
    
    # 创建测试套件
    test_suite = unittest.TestSuite()
    
    # 添加测试用例
    test_suite.addTest(unittest.makeSuite(TestAgent))
    test_suite.addTest(unittest.makeSuite(TestAgentIntegration))
    
    # 运行测试
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(test_suite)
    
    # 输出结果
    if result.wasSuccessful():
        print("\n✅ 所有测试通过！")
    else:
        print(f"\n❌ 测试失败: {len(result.failures)} 个失败, {len(result.errors)} 个错误")
    
    return result.wasSuccessful()


if __name__ == "__main__":
    run_tests()
