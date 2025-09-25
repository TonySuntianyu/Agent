"""
LangGraph Agent使用示例
"""
import os
from agent import LangGraphAgent


def main():
    """主函数"""
    print("=== LangGraph Agent 示例 ===\n")
    
    # 创建Agent实例
    agent = LangGraphAgent()
    
    # 示例1: 数学计算
    print("示例1: 数学计算")
    print("问题: 计算 2^10 + 3*5 的结果")
    result1 = agent.chat("计算 2^10 + 3*5 的结果")
    print(f"回答: {result1}\n")
    
    # 示例2: 文件操作
    print("示例2: 文件操作")
    print("问题: 列出当前目录的文件")
    result2 = agent.chat("列出当前目录的文件")
    print(f"回答: {result2}\n")
    
    # 示例3: 时间查询
    print("示例3: 时间查询")
    print("问题: 现在几点了？")
    result3 = agent.chat("现在几点了？")
    print(f"回答: {result3}\n")
    
    # 示例4: 数据分析
    print("示例4: 数据分析")
    print("问题: 分析数据 [1,2,3,4,5,6,7,8,9,10] 的统计信息")
    data = [{"value": i} for i in range(1, 11)]
    import json
    data_str = json.dumps(data)
    result4 = agent.chat(f"分析数据 {data_str} 的统计信息")
    print(f"回答: {result4}\n")
    
    # 示例5: 复杂任务
    print("示例5: 复杂任务")
    print("问题: 计算当前时间的Unix时间戳，然后计算这个时间戳的平方根")
    result5 = agent.chat("计算当前时间的Unix时间戳，然后计算这个时间戳的平方根")
    print(f"回答: {result5}\n")


def interactive_chat():
    """交互式聊天"""
    print("=== 交互式聊天模式 ===")
    print("输入 'quit' 退出\n")
    
    agent = LangGraphAgent()
    
    while True:
        user_input = input("您: ")
        if user_input.lower() == 'quit':
            print("再见！")
            break
        
        response = agent.chat(user_input)
        print(f"Agent: {response}\n")


if __name__ == "__main__":
    # 检查环境变量
    if not os.getenv("OPENAI_API_KEY"):
        print("请设置OPENAI_API_KEY环境变量")
        print("您可以在.env文件中设置，或者直接设置环境变量")
        exit(1)
    
    # 运行示例
    main()
    
    # 询问是否进入交互模式
    choice = input("是否进入交互式聊天模式？(y/n): ")
    if choice.lower() == 'y':
        interactive_chat()
