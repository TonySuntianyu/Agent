"""
图书推荐相关工具
"""
import json
import requests
from typing import Dict, Any, List, Optional
from datetime import datetime
import random


class BookDatabase:
    """模拟图书数据库"""
    
    def __init__(self):
        self.books = self._initialize_books()
        self.knowledge_graph = self._build_knowledge_graph()
    
    def _initialize_books(self) -> List[Dict[str, Any]]:
        """初始化图书数据"""
        return [
            {
                "title": "三体",
                "author": "刘慈欣",
                "isbn": "9787536692930",
                "genre": "科幻",
                "rating": 9.0,
                "description": "地球文明向宇宙发出第一声啼鸣，取得了探寻外星文明的突破性进展。",
                "publication_year": 2006,
                "publisher": "重庆出版社"
            },
            {
                "title": "流浪地球",
                "author": "刘慈欣",
                "isbn": "9787536692931",
                "genre": "科幻",
                "rating": 8.5,
                "description": "太阳即将毁灭，人类在地球表面建造出巨大的推进器，寻找新家园。",
                "publication_year": 2008,
                "publisher": "重庆出版社"
            },
            {
                "title": "球状闪电",
                "author": "刘慈欣",
                "isbn": "9787536692932",
                "genre": "科幻",
                "rating": 8.2,
                "description": "一个关于球状闪电的科幻故事。",
                "publication_year": 2004,
                "publisher": "重庆出版社"
            },
            {
                "title": "活着",
                "author": "余华",
                "isbn": "9787506365437",
                "genre": "文学",
                "rating": 9.2,
                "description": "讲述了在大时代背景下，随着内战、三反五反，大跃进，文化大革命等社会变革。",
                "publication_year": 1993,
                "publisher": "作家出版社"
            },
            {
                "title": "许三观卖血记",
                "author": "余华",
                "isbn": "9787506365438",
                "genre": "文学",
                "rating": 8.8,
                "description": "讲述了许三观靠着卖血渡过了人生的一个个难关。",
                "publication_year": 1995,
                "publisher": "作家出版社"
            },
            {
                "title": "百年孤独",
                "author": "加西亚·马尔克斯",
                "isbn": "9787544253994",
                "genre": "魔幻现实主义",
                "rating": 9.3,
                "description": "描述了布恩迪亚家族七代人的传奇故事。",
                "publication_year": 1967,
                "publisher": "南海出版公司"
            },
            {
                "title": "霍乱时期的爱情",
                "author": "加西亚·马尔克斯",
                "isbn": "9787544253995",
                "genre": "魔幻现实主义",
                "rating": 8.9,
                "description": "讲述了一段跨越半个多世纪的爱情史诗。",
                "publication_year": 1985,
                "publisher": "南海出版公司"
            },
            {
                "title": "1984",
                "author": "乔治·奥威尔",
                "isbn": "9787532749519",
                "genre": "反乌托邦",
                "rating": 9.1,
                "description": "描绘了一个极权主义社会的恐怖景象。",
                "publication_year": 1949,
                "publisher": "译林出版社"
            },
            {
                "title": "动物农场",
                "author": "乔治·奥威尔",
                "isbn": "9787532749520",
                "genre": "反乌托邦",
                "rating": 8.7,
                "description": "以动物为主角的政治寓言小说。",
                "publication_year": 1945,
                "publisher": "译林出版社"
            },
            {
                "title": "解忧杂货店",
                "author": "东野圭吾",
                "isbn": "9787544270878",
                "genre": "推理小说",
                "rating": 8.6,
                "description": "讲述了在僻静街道旁的一家杂货店，只要写下烦恼投进店前门卷帘门的投信口。",
                "publication_year": 2012,
                "publisher": "南海出版公司"
            }
        ]
    
    def _build_knowledge_graph(self) -> Dict[str, Any]:
        """构建知识图谱"""
        return {
            "authors": {
                "刘慈欣": {
                    "genres": ["科幻"],
                    "books": ["三体", "流浪地球", "球状闪电"],
                    "style": "硬科幻"
                },
                "余华": {
                    "genres": ["文学"],
                    "books": ["活着", "许三观卖血记"],
                    "style": "现实主义"
                },
                "加西亚·马尔克斯": {
                    "genres": ["魔幻现实主义"],
                    "books": ["百年孤独", "霍乱时期的爱情"],
                    "style": "魔幻现实主义"
                },
                "乔治·奥威尔": {
                    "genres": ["反乌托邦"],
                    "books": ["1984", "动物农场"],
                    "style": "政治讽刺"
                },
                "东野圭吾": {
                    "genres": ["推理小说"],
                    "books": ["解忧杂货店"],
                    "style": "悬疑推理"
                }
            },
            "genres": {
                "科幻": {
                    "authors": ["刘慈欣"],
                    "similar_genres": ["魔幻现实主义", "反乌托邦"]
                },
                "文学": {
                    "authors": ["余华"],
                    "similar_genres": ["魔幻现实主义"]
                },
                "魔幻现实主义": {
                    "authors": ["加西亚·马尔克斯"],
                    "similar_genres": ["文学", "科幻"]
                },
                "反乌托邦": {
                    "authors": ["乔治·奥威尔"],
                    "similar_genres": ["科幻"]
                },
                "推理小说": {
                    "authors": ["东野圭吾"],
                    "similar_genres": ["文学"]
                }
            }
        }
    
    def search_books(self, query: str, limit: int = 10) -> List[Dict[str, Any]]:
        """搜索图书"""
        results = []
        query_lower = query.lower()
        
        for book in self.books:
            if (query_lower in book["title"].lower() or 
                query_lower in book["author"].lower() or 
                query_lower in book["genre"].lower() or
                query_lower in book["description"].lower()):
                results.append(book)
        
        return results[:limit]
    
    def get_book_by_title(self, title: str) -> Optional[Dict[str, Any]]:
        """根据标题获取图书"""
        for book in self.books:
            if book["title"] == title:
                return book
        return None
    
    def get_books_by_author(self, author: str) -> List[Dict[str, Any]]:
        """根据作者获取图书"""
        return [book for book in self.books if book["author"] == author]
    
    def get_books_by_genre(self, genre: str) -> List[Dict[str, Any]]:
        """根据类型获取图书"""
        return [book for book in self.books if book["genre"] == genre]


class BookRecommendationTool:
    """图书推荐工具"""
    
    def __init__(self):
        self.db = BookDatabase()
    
    def recommend_by_author(self, author: str, exclude_books: List[str] = None) -> Dict[str, Any]:
        """根据作者推荐图书"""
        if exclude_books is None:
            exclude_books = []
        
        books = self.db.get_books_by_author(author)
        recommendations = [book for book in books if book["title"] not in exclude_books]
        
        return {
            "success": True,
            "recommendations": recommendations,
            "reason": f"推荐作者 {author} 的其他作品",
            "count": len(recommendations)
        }
    
    def recommend_by_genre(self, genre: str, exclude_books: List[str] = None) -> Dict[str, Any]:
        """根据类型推荐图书"""
        if exclude_books is None:
            exclude_books = []
        
        books = self.db.get_books_by_genre(genre)
        recommendations = [book for book in books if book["title"] not in exclude_books]
        
        return {
            "success": True,
            "recommendations": recommendations,
            "reason": f"推荐 {genre} 类型的其他图书",
            "count": len(recommendations)
        }
    
    def recommend_by_knowledge_graph(self, current_book: Dict[str, Any]) -> Dict[str, Any]:
        """基于知识图谱推荐图书"""
        recommendations = []
        reasons = []
        
        # 获取当前图书信息
        title = current_book["title"]
        author = current_book["author"]
        genre = current_book["genre"]
        
        # 1. 推荐同作者其他作品
        author_books = self.db.get_books_by_author(author)
        author_recommendations = [book for book in author_books if book["title"] != title]
        if author_recommendations:
            recommendations.extend(author_recommendations[:2])
            reasons.append(f"同作者 {author} 的其他作品")
        
        # 2. 推荐同类型其他图书
        genre_books = self.db.get_books_by_genre(genre)
        genre_recommendations = [book for book in genre_books if book["title"] != title]
        if genre_recommendations:
            recommendations.extend(genre_recommendations[:2])
            reasons.append(f"同类型 {genre} 的其他图书")
        
        # 3. 基于知识图谱推荐相似类型
        kg = self.db.knowledge_graph
        if genre in kg["genres"]:
            similar_genres = kg["genres"][genre].get("similar_genres", [])
            for similar_genre in similar_genres:
                similar_books = self.db.get_books_by_genre(similar_genre)
                if similar_books:
                    recommendations.extend(similar_books[:1])
                    reasons.append(f"相似类型 {similar_genre} 的图书")
        
        # 去重
        seen_titles = set()
        unique_recommendations = []
        for book in recommendations:
            if book["title"] not in seen_titles:
                unique_recommendations.append(book)
                seen_titles.add(book["title"])
        
        return {
            "success": True,
            "recommendations": unique_recommendations[:5],
            "reasons": reasons,
            "count": len(unique_recommendations)
        }
    
    def get_user_preferences(self, user_id: str) -> Dict[str, Any]:
        """获取用户偏好（模拟）"""
        # 这里应该从数据库获取真实用户偏好
        # 现在返回模拟数据
        return {
            "success": True,
            "preferences": {
                "favorite_genres": ["科幻", "文学"],
                "favorite_authors": ["刘慈欣", "余华"],
                "reading_history": [],
                "preferred_rating": 8.5
            }
        }
    
    def update_user_preferences(self, user_id: str, book_info: Dict[str, Any]) -> Dict[str, Any]:
        """更新用户偏好"""
        # 这里应该更新数据库中的用户偏好
        return {
            "success": True,
            "message": f"已记录用户对图书《{book_info['title']}》的浏览"
        }


class BookSearchTool:
    """图书搜索工具"""
    
    def __init__(self):
        self.db = BookDatabase()
    
    def search_books(self, query: str, limit: int = 10) -> Dict[str, Any]:
        """搜索图书"""
        results = self.db.search_books(query, limit)
        return {
            "success": True,
            "query": query,
            "results": results,
            "count": len(results)
        }
    
    def get_book_details(self, title: str) -> Dict[str, Any]:
        """获取图书详细信息"""
        book = self.db.get_book_by_title(title)
        if book:
            return {
                "success": True,
                "book": book
            }
        else:
            return {
                "success": False,
                "error": f"未找到图书《{title}》"
            }


class BookAnalysisTool:
    """图书分析工具"""
    
    def __init__(self):
        self.db = BookDatabase()
    
    def analyze_reading_trends(self, user_history: List[Dict[str, Any]]) -> Dict[str, Any]:
        """分析用户阅读趋势"""
        if not user_history:
            return {
                "success": False,
                "error": "用户阅读历史为空"
            }
        
        # 分析最喜欢的类型
        genre_count = {}
        author_count = {}
        
        for book in user_history:
            genre = book.get("genre", "未知")
            author = book.get("author", "未知")
            
            genre_count[genre] = genre_count.get(genre, 0) + 1
            author_count[author] = author_count.get(author, 0) + 1
        
        favorite_genre = max(genre_count.items(), key=lambda x: x[1])[0] if genre_count else "未知"
        favorite_author = max(author_count.items(), key=lambda x: x[1])[0] if author_count else "未知"
        
        return {
            "success": True,
            "analysis": {
                "total_books": len(user_history),
                "favorite_genre": favorite_genre,
                "favorite_author": favorite_author,
                "genre_distribution": genre_count,
                "author_distribution": author_count
            }
        }
    
    def get_similar_books(self, book_info: Dict[str, Any]) -> Dict[str, Any]:
        """获取相似图书"""
        title = book_info["title"]
        author = book_info["author"]
        genre = book_info["genre"]
        
        # 基于多种因素计算相似度
        similar_books = []
        
        # 同作者其他作品
        author_books = self.db.get_books_by_author(author)
        for book in author_books:
            if book["title"] != title:
                similar_books.append({
                    "book": book,
                    "similarity_reason": "同作者",
                    "similarity_score": 0.9
                })
        
        # 同类型其他图书
        genre_books = self.db.get_books_by_genre(genre)
        for book in genre_books:
            if book["title"] != title:
                similar_books.append({
                    "book": book,
                    "similarity_reason": "同类型",
                    "similarity_score": 0.8
                })
        
        # 按相似度排序
        similar_books.sort(key=lambda x: x["similarity_score"], reverse=True)
        
        return {
            "success": True,
            "similar_books": similar_books[:5],
            "count": len(similar_books)
        }


# 工具实例
book_db = BookDatabase()
book_recommendation_tool = BookRecommendationTool()
book_search_tool = BookSearchTool()
book_analysis_tool = BookAnalysisTool()