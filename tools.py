"""
工具函数集合
"""
import requests
import json
import math
import os
from typing import Dict, Any, List
from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


class CalculatorTool:
    """计算器工具"""
    
    @staticmethod
    def calculate(expression: str) -> Dict[str, Any]:
        """安全地计算数学表达式"""
        try:
            # 只允许安全的数学操作
            allowed_names = {
                k: v for k, v in math.__dict__.items() if not k.startswith("__")
            }
            allowed_names.update({
                "abs": abs, "round": round, "min": min, "max": max,
                "sum": sum, "pow": pow
            })
            
            result = eval(expression, {"__builtins__": {}}, allowed_names)
            return {
                "success": True,
                "result": result,
                "expression": expression
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "expression": expression
            }


class WebSearchTool:
    """网络搜索工具"""
    
    def __init__(self, api_key: str = None):
        self.api_key = api_key
    
    def search(self, query: str, num_results: int = 5) -> Dict[str, Any]:
        """搜索网络信息"""
        try:
            if self.api_key:
                # 使用Serper API进行搜索
                url = "https://google.serper.dev/search"
                headers = {
                    "X-API-KEY": self.api_key,
                    "Content-Type": "application/json"
                }
                data = {
                    "q": query,
                    "num": num_results
                }
                response = requests.post(url, headers=headers, json=data)
                results = response.json()
                
                return {
                    "success": True,
                    "query": query,
                    "results": results.get("organic", [])[:num_results]
                }
            else:
                # 模拟搜索结果
                return {
                    "success": True,
                    "query": query,
                    "results": [
                        {
                            "title": f"搜索结果 {i+1}",
                            "snippet": f"这是关于'{query}'的搜索结果摘要 {i+1}",
                            "link": f"https://example.com/result{i+1}"
                        }
                        for i in range(num_results)
                    ]
                }
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "query": query
            }


class FileTool:
    """文件操作工具"""
    
    @staticmethod
    def read_file(file_path: str) -> Dict[str, Any]:
        """读取文件内容"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            return {
                "success": True,
                "content": content,
                "file_path": file_path
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "file_path": file_path
            }
    
    @staticmethod
    def write_file(file_path: str, content: str) -> Dict[str, Any]:
        """写入文件内容"""
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return {
                "success": True,
                "file_path": file_path,
                "message": "文件写入成功"
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "file_path": file_path
            }
    
    @staticmethod
    def list_files(directory: str = ".") -> Dict[str, Any]:
        """列出目录中的文件"""
        try:
            files = os.listdir(directory)
            return {
                "success": True,
                "files": files,
                "directory": directory
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "directory": directory
            }


class DataAnalysisTool:
    """数据分析工具"""
    
    @staticmethod
    def create_chart(data: List[Dict], chart_type: str = "line") -> Dict[str, Any]:
        """创建图表"""
        try:
            if not data:
                return {"success": False, "error": "数据为空"}
            
            # 创建DataFrame
            df = pd.DataFrame(data)
            
            # 创建图表
            plt.figure(figsize=(10, 6))
            
            if chart_type == "line":
                for column in df.columns:
                    if df[column].dtype in ['int64', 'float64']:
                        plt.plot(df.index, df[column], label=column)
            elif chart_type == "bar":
                df.plot(kind='bar')
            elif chart_type == "scatter":
                if len(df.columns) >= 2:
                    plt.scatter(df.iloc[:, 0], df.iloc[:, 1])
            
            plt.title("数据分析图表")
            plt.legend()
            plt.grid(True)
            
            # 保存图表
            chart_path = f"chart_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
            plt.savefig(chart_path)
            plt.close()
            
            return {
                "success": True,
                "chart_path": chart_path,
                "chart_type": chart_type
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }
    
    @staticmethod
    def analyze_data(data: List[Dict]) -> Dict[str, Any]:
        """分析数据统计信息"""
        try:
            if not data:
                return {"success": False, "error": "数据为空"}
            
            df = pd.DataFrame(data)
            
            # 计算统计信息
            stats = {}
            for column in df.columns:
                if df[column].dtype in ['int64', 'float64']:
                    stats[column] = {
                        "mean": float(df[column].mean()),
                        "median": float(df[column].median()),
                        "std": float(df[column].std()),
                        "min": float(df[column].min()),
                        "max": float(df[column].max()),
                        "count": int(df[column].count())
                    }
            
            return {
                "success": True,
                "statistics": stats,
                "data_shape": df.shape
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }


class TimeTool:
    """时间工具"""
    
    @staticmethod
    def get_current_time() -> Dict[str, Any]:
        """获取当前时间"""
        now = datetime.now()
        return {
            "success": True,
            "current_time": now.strftime("%Y-%m-%d %H:%M:%S"),
            "timestamp": now.timestamp(),
            "date": now.strftime("%Y-%m-%d"),
            "time": now.strftime("%H:%M:%S")
        }
    
    @staticmethod
    def format_time(timestamp: float, format_str: str = "%Y-%m-%d %H:%M:%S") -> Dict[str, Any]:
        """格式化时间戳"""
        try:
            dt = datetime.fromtimestamp(timestamp)
            formatted = dt.strftime(format_str)
            return {
                "success": True,
                "formatted_time": formatted,
                "timestamp": timestamp
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "timestamp": timestamp
            }


# 工具注册表
TOOLS = {
    "calculator": CalculatorTool(),
    "web_search": WebSearchTool(),
    "file": FileTool(),
    "data_analysis": DataAnalysisTool(),
    "time": TimeTool()
}
