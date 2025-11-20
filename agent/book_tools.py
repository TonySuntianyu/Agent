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
            },
            {
                "title": "白夜行",
                "author": "东野圭吾",
                "isbn": "9787544258609",
                "genre": "推理小说",
                "rating": 9.1,
                "description": "一部关于绝望与希望的推理小说，讲述了两个孩子的悲剧命运。",
                "publication_year": 1999,
                "publisher": "南海出版公司"
            },
            {
                "title": "嫌疑人X的献身",
                "author": "东野圭吾",
                "isbn": "9787544258616",
                "genre": "推理小说",
                "rating": 8.9,
                "description": "一个数学天才为了帮助邻居掩盖罪行而精心设计的完美犯罪。",
                "publication_year": 2005,
                "publisher": "南海出版公司"
            },
            {
                "title": "挪威的森林",
                "author": "村上春树",
                "isbn": "9787532742923",
                "genre": "文学",
                "rating": 8.8,
                "description": "一部关于青春、爱情和成长的青春小说。",
                "publication_year": 1987,
                "publisher": "上海译文出版社"
            },
            {
                "title": "1Q84",
                "author": "村上春树",
                "isbn": "9787532754681",
                "genre": "文学",
                "rating": 8.5,
                "description": "一个充满悬疑和奇幻色彩的长篇小说。",
                "publication_year": 2009,
                "publisher": "南海出版公司"
            },
            {
                "title": "海边的卡夫卡",
                "author": "村上春树",
                "isbn": "9787532742924",
                "genre": "文学",
                "rating": 8.7,
                "description": "一个15岁少年的成长故事，充满超现实主义的色彩。",
                "publication_year": 2002,
                "publisher": "上海译文出版社"
            },
            {
                "title": "红高粱",
                "author": "莫言",
                "isbn": "9787020008739",
                "genre": "文学",
                "rating": 8.9,
                "description": "以抗日战争为背景，讲述了一个家族三代人的故事。",
                "publication_year": 1987,
                "publisher": "人民文学出版社"
            },
            {
                "title": "丰乳肥臀",
                "author": "莫言",
                "isbn": "9787020008740",
                "genre": "文学",
                "rating": 8.6,
                "description": "通过一个家族的兴衰，展现了中国近现代历史的变迁。",
                "publication_year": 1995,
                "publisher": "作家出版社"
            },
            {
                "title": "蛙",
                "author": "莫言",
                "isbn": "9787020008741",
                "genre": "文学",
                "rating": 8.4,
                "description": "以计划生育为背景，讲述了一个乡村医生的故事。",
                "publication_year": 2009,
                "publisher": "上海文艺出版社"
            },
            {
                "title": "平凡的世界",
                "author": "路遥",
                "isbn": "9787020008738",
                "genre": "文学",
                "rating": 9.2,
                "description": "一部全景式地表现中国当代城乡社会生活的长篇小说。",
                "publication_year": 1986,
                "publisher": "人民文学出版社"
            },
            {
                "title": "人生",
                "author": "路遥",
                "isbn": "9787020008737",
                "genre": "文学",
                "rating": 8.7,
                "description": "讲述了一个农村青年在人生道路上的选择与挣扎。",
                "publication_year": 1982,
                "publisher": "人民文学出版社"
            },
            {
                "title": "黄金时代",
                "author": "王小波",
                "isbn": "9787532733441",
                "genre": "文学",
                "rating": 9.0,
                "description": "以文革为背景，讲述了一个知识分子的荒诞经历。",
                "publication_year": 1991,
                "publisher": "花城出版社"
            },
            {
                "title": "沉默的大多数",
                "author": "王小波",
                "isbn": "9787532733442",
                "genre": "杂文",
                "rating": 8.8,
                "description": "王小波的杂文代表作，展现了他独特的思考方式。",
                "publication_year": 1997,
                "publisher": "中国青年出版社"
            },
            {
                "title": "围城",
                "author": "钱钟书",
                "isbn": "9787020008736",
                "genre": "文学",
                "rating": 9.1,
                "description": "一部讽刺小说，描绘了抗战初期知识分子的群像。",
                "publication_year": 1947,
                "publisher": "人民文学出版社"
            },
            {
                "title": "边城",
                "author": "沈从文",
                "isbn": "9787020008735",
                "genre": "文学",
                "rating": 8.9,
                "description": "以湘西为背景，讲述了一个纯美的爱情故事。",
                "publication_year": 1934,
                "publisher": "人民文学出版社"
            },
            {
                "title": "老人与海",
                "author": "海明威",
                "isbn": "9787532742925",
                "genre": "文学",
                "rating": 8.8,
                "description": "一个老渔夫与一条大鱼的搏斗，展现了人的尊严和勇气。",
                "publication_year": 1952,
                "publisher": "上海译文出版社"
            },
            {
                "title": "太阳照常升起",
                "author": "海明威",
                "isbn": "9787532742926",
                "genre": "文学",
                "rating": 8.5,
                "description": "描写了一战后一群流落欧洲的美国青年的生活。",
                "publication_year": 1926,
                "publisher": "上海译文出版社"
            },
            {
                "title": "变形记",
                "author": "卡夫卡",
                "isbn": "9787532742927",
                "genre": "文学",
                "rating": 8.9,
                "description": "一个人变成甲虫的荒诞故事，反映了现代人的异化。",
                "publication_year": 1915,
                "publisher": "上海译文出版社"
            },
            {
                "title": "城堡",
                "author": "卡夫卡",
                "isbn": "9787532742928",
                "genre": "文学",
                "rating": 8.7,
                "description": "一个土地测量员试图进入城堡的故事，充满象征意义。",
                "publication_year": 1926,
                "publisher": "上海译文出版社"
            },
            {
                "title": "追风筝的人",
                "author": "卡勒德·胡赛尼",
                "isbn": "9787532742929",
                "genre": "文学",
                "rating": 8.9,
                "description": "一个关于友谊、背叛和救赎的故事。",
                "publication_year": 2003,
                "publisher": "上海人民出版社"
            },
            {
                "title": "灿烂千阳",
                "author": "卡勒德·胡赛尼",
                "isbn": "9787532742930",
                "genre": "文学",
                "rating": 8.7,
                "description": "两个阿富汗女性的故事，展现了战争对女性的影响。",
                "publication_year": 2007,
                "publisher": "上海人民出版社"
            },
            {
                "title": "小王子",
                "author": "安托万·德·圣埃克苏佩里",
                "isbn": "9787532742931",
                "genre": "童话",
                "rating": 9.3,
                "description": "一部写给大人的童话，探讨了爱与责任的主题。",
                "publication_year": 1943,
                "publisher": "人民文学出版社"
            },
            {
                "title": "月亮与六便士",
                "author": "毛姆",
                "isbn": "9787532742932",
                "genre": "文学",
                "rating": 8.8,
                "description": "一个证券经纪人放弃一切追求艺术梦想的故事。",
                "publication_year": 1919,
                "publisher": "上海译文出版社"
            },
            {
                "title": "人性的枷锁",
                "author": "毛姆",
                "isbn": "9787532742933",
                "genre": "文学",
                "rating": 8.6,
                "description": "一个青年的成长历程，探讨了人生的意义。",
                "publication_year": 1915,
                "publisher": "上海译文出版社"
            },
            {
                "title": "局外人",
                "author": "阿尔贝·加缪",
                "isbn": "9787532742934",
                "genre": "文学",
                "rating": 9.0,
                "description": "一个对生活漠不关心的人的故事，探讨了存在的荒诞性。",
                "publication_year": 1942,
                "publisher": "上海译文出版社"
            },
            {
                "title": "鼠疫",
                "author": "阿尔贝·加缪",
                "isbn": "9787532742935",
                "genre": "文学",
                "rating": 8.9,
                "description": "一个城市爆发鼠疫的故事，展现了人类面对灾难的勇气。",
                "publication_year": 1947,
                "publisher": "上海译文出版社"
            },
            {
                "title": "麦田里的守望者",
                "author": "J.D.塞林格",
                "isbn": "9787532742936",
                "genre": "文学",
                "rating": 8.7,
                "description": "一个16岁少年的内心独白，反映了青少年的迷茫和反叛。",
                "publication_year": 1951,
                "publisher": "译林出版社"
            },
            {
                "title": "了不起的盖茨比",
                "author": "F.斯科特·菲茨杰拉德",
                "isbn": "9787532742937",
                "genre": "文学",
                "rating": 8.8,
                "description": "一个关于美国梦的破灭的故事。",
                "publication_year": 1925,
                "publisher": "上海译文出版社"
            },
            {
                "title": "杀死一只知更鸟",
                "author": "哈珀·李",
                "isbn": "9787532742938",
                "genre": "文学",
                "rating": 9.2,
                "description": "一个关于种族歧视和正义的故事，通过孩子的视角展现。",
                "publication_year": 1960,
                "publisher": "译林出版社"
            },
            {
                "title": "飘",
                "author": "玛格丽特·米切尔",
                "isbn": "9787532742939",
                "genre": "文学",
                "rating": 9.0,
                "description": "以美国南北战争为背景，讲述了一个女性的成长故事。",
                "publication_year": 1936,
                "publisher": "译林出版社"
            },
            {
                "title": "简·爱",
                "author": "夏洛蒂·勃朗特",
                "isbn": "9787532742940",
                "genre": "文学",
                "rating": 8.9,
                "description": "一个独立女性的成长故事，追求自由和平等。",
                "publication_year": 1847,
                "publisher": "人民文学出版社"
            },
            {
                "title": "呼啸山庄",
                "author": "艾米莉·勃朗特",
                "isbn": "9787532742941",
                "genre": "文学",
                "rating": 8.8,
                "description": "一个关于复仇和爱情的哥特式小说。",
                "publication_year": 1847,
                "publisher": "人民文学出版社"
            },
            {
                "title": "傲慢与偏见",
                "author": "简·奥斯汀",
                "isbn": "9787532742942",
                "genre": "文学",
                "rating": 9.1,
                "description": "一部经典的爱情小说，探讨了社会阶层和婚姻。",
                "publication_year": 1813,
                "publisher": "人民文学出版社"
            },
            {
                "title": "罪与罚",
                "author": "陀思妥耶夫斯基",
                "isbn": "9787532742943",
                "genre": "文学",
                "rating": 9.2,
                "description": "一个大学生犯罪后的心理挣扎和救赎。",
                "publication_year": 1866,
                "publisher": "人民文学出版社"
            },
            {
                "title": "战争与和平",
                "author": "列夫·托尔斯泰",
                "isbn": "9787532742944",
                "genre": "文学",
                "rating": 9.3,
                "description": "以拿破仑战争为背景，展现了俄国社会的全景。",
                "publication_year": 1869,
                "publisher": "人民文学出版社"
            },
            {
                "title": "安娜·卡列尼娜",
                "author": "列夫·托尔斯泰",
                "isbn": "9787532742945",
                "genre": "文学",
                "rating": 9.2,
                "description": "一个已婚女性的爱情悲剧，反映了俄国社会的道德观念。",
                "publication_year": 1877,
                "publisher": "人民文学出版社"
            },
            {
                "title": "复活",
                "author": "列夫·托尔斯泰",
                "isbn": "9787532742946",
                "genre": "文学",
                "rating": 8.9,
                "description": "一个贵族青年的精神复活，探讨了道德和救赎。",
                "publication_year": 1899,
                "publisher": "人民文学出版社"
            },
            {
                "title": "红楼梦",
                "author": "曹雪芹",
                "isbn": "9787020002207",
                "genre": "古典文学",
                "rating": 9.6,
                "description": "中国古典四大名著之一，以贾、史、王、薛四大家族的兴衰为背景，展现了封建社会的全貌。",
                "publication_year": 1791,
                "publisher": "人民文学出版社"
            },
            {
                "title": "西游记",
                "author": "吴承恩",
                "isbn": "9787020008735",
                "genre": "古典文学",
                "rating": 9.4,
                "description": "中国古典四大名著之一，讲述了唐僧师徒四人西天取经的故事。",
                "publication_year": 1592,
                "publisher": "人民文学出版社"
            },
            {
                "title": "水浒传",
                "author": "施耐庵",
                "isbn": "9787020008736",
                "genre": "古典文学",
                "rating": 9.3,
                "description": "中国古典四大名著之一，描写了108位好汉在梁山泊聚义的故事。",
                "publication_year": 1589,
                "publisher": "人民文学出版社"
            },
            {
                "title": "三国演义",
                "author": "罗贯中",
                "isbn": "9787020008737",
                "genre": "古典文学",
                "rating": 9.5,
                "description": "中国古典四大名著之一，以三国时期的历史为背景，展现了英雄辈出的时代。",
                "publication_year": 1522,
                "publisher": "人民文学出版社"
            },
            {
                "title": "呐喊",
                "author": "鲁迅",
                "isbn": "9787020008742",
                "genre": "文学",
                "rating": 9.2,
                "description": "鲁迅的短篇小说集，包括《狂人日记》、《阿Q正传》等经典作品。",
                "publication_year": 1923,
                "publisher": "人民文学出版社"
            },
            {
                "title": "彷徨",
                "author": "鲁迅",
                "isbn": "9787020008743",
                "genre": "文学",
                "rating": 9.0,
                "description": "鲁迅的第二部短篇小说集，反映了五四运动后知识分子的迷茫。",
                "publication_year": 1926,
                "publisher": "人民文学出版社"
            },
            {
                "title": "朝花夕拾",
                "author": "鲁迅",
                "isbn": "9787020008744",
                "genre": "散文",
                "rating": 8.9,
                "description": "鲁迅的散文集，回忆了童年和青少年时期的生活。",
                "publication_year": 1928,
                "publisher": "人民文学出版社"
            },
            {
                "title": "家",
                "author": "巴金",
                "isbn": "9787020008745",
                "genre": "文学",
                "rating": 8.8,
                "description": "激流三部曲之一，描写了一个封建大家庭的衰落。",
                "publication_year": 1933,
                "publisher": "人民文学出版社"
            },
            {
                "title": "春",
                "author": "巴金",
                "isbn": "9787020008746",
                "genre": "文学",
                "rating": 8.7,
                "description": "激流三部曲之二，继续描写封建家庭的命运。",
                "publication_year": 1938,
                "publisher": "人民文学出版社"
            },
            {
                "title": "秋",
                "author": "巴金",
                "isbn": "9787020008747",
                "genre": "文学",
                "rating": 8.7,
                "description": "激流三部曲之三，封建大家庭的最终结局。",
                "publication_year": 1940,
                "publisher": "人民文学出版社"
            },
            {
                "title": "骆驼祥子",
                "author": "老舍",
                "isbn": "9787020008748",
                "genre": "文学",
                "rating": 9.1,
                "description": "描写了北京人力车夫祥子的悲惨命运。",
                "publication_year": 1936,
                "publisher": "人民文学出版社"
            },
            {
                "title": "茶馆",
                "author": "老舍",
                "isbn": "9787020008749",
                "genre": "戏剧",
                "rating": 9.0,
                "description": "通过茶馆的变迁，展现了从清末到解放前夕的社会变迁。",
                "publication_year": 1957,
                "publisher": "人民文学出版社"
            },
            {
                "title": "雷雨",
                "author": "曹禺",
                "isbn": "9787020008750",
                "genre": "戏剧",
                "rating": 9.1,
                "description": "一部经典的现代话剧，描写了一个封建家庭的悲剧。",
                "publication_year": 1934,
                "publisher": "人民文学出版社"
            },
            {
                "title": "子夜",
                "author": "茅盾",
                "isbn": "9787020008751",
                "genre": "文学",
                "rating": 8.9,
                "description": "描写了20世纪30年代上海的民族工业发展。",
                "publication_year": 1933,
                "publisher": "人民文学出版社"
            },
            {
                "title": "边城",
                "author": "沈从文",
                "isbn": "9787020008752",
                "genre": "文学",
                "rating": 8.9,
                "description": "以湘西为背景，讲述了一个纯美的爱情故事。",
                "publication_year": 1934,
                "publisher": "人民文学出版社"
            },
            {
                "title": "围城",
                "author": "钱钟书",
                "isbn": "9787020008753",
                "genre": "文学",
                "rating": 9.1,
                "description": "一部讽刺小说，描绘了抗战初期知识分子的群像。",
                "publication_year": 1947,
                "publisher": "人民文学出版社"
            },
            {
                "title": "白鹿原",
                "author": "陈忠实",
                "isbn": "9787020008754",
                "genre": "文学",
                "rating": 9.2,
                "description": "以陕西关中地区为背景，展现了从清末到解放初期的历史变迁。",
                "publication_year": 1993,
                "publisher": "人民文学出版社"
            },
            {
                "title": "长恨歌",
                "author": "王安忆",
                "isbn": "9787020008755",
                "genre": "文学",
                "rating": 8.8,
                "description": "以上海为背景，讲述了一个女性的一生。",
                "publication_year": 1995,
                "publisher": "人民文学出版社"
            },
            {
                "title": "蛙",
                "author": "莫言",
                "isbn": "9787020008756",
                "genre": "文学",
                "rating": 8.4,
                "description": "以计划生育为背景，讲述了一个乡村医生的故事。",
                "publication_year": 2009,
                "publisher": "上海文艺出版社"
            },
            {
                "title": "檀香刑",
                "author": "莫言",
                "isbn": "9787020008757",
                "genre": "文学",
                "rating": 8.6,
                "description": "以清末为背景，描写了残酷的刑罚和人性。",
                "publication_year": 2001,
                "publisher": "作家出版社"
            },
            {
                "title": "生死疲劳",
                "author": "莫言",
                "isbn": "9787020008758",
                "genre": "文学",
                "rating": 8.7,
                "description": "一个地主转世为各种动物的荒诞故事。",
                "publication_year": 2006,
                "publisher": "作家出版社"
            },
            {
                "title": "兄弟",
                "author": "余华",
                "isbn": "9787020008759",
                "genre": "文学",
                "rating": 8.5,
                "description": "讲述了两个兄弟从文革到改革开放的人生历程。",
                "publication_year": 2005,
                "publisher": "作家出版社"
            },
            {
                "title": "在细雨中呼喊",
                "author": "余华",
                "isbn": "9787020008760",
                "genre": "文学",
                "rating": 8.6,
                "description": "一个少年的成长故事，展现了人性的复杂。",
                "publication_year": 1991,
                "publisher": "作家出版社"
            },
            {
                "title": "第七天",
                "author": "余华",
                "isbn": "9787020008761",
                "genre": "文学",
                "rating": 8.3,
                "description": "一个死者在死后七天的见闻，反映了社会现实。",
                "publication_year": 2013,
                "publisher": "作家出版社"
            },
            {
                "title": "三体II：黑暗森林",
                "author": "刘慈欣",
                "isbn": "9787536692933",
                "genre": "科幻",
                "rating": 9.2,
                "description": "三体系列的第二部，探讨了宇宙文明的生存法则。",
                "publication_year": 2008,
                "publisher": "重庆出版社"
            },
            {
                "title": "三体III：死神永生",
                "author": "刘慈欣",
                "isbn": "9787536692934",
                "genre": "科幻",
                "rating": 9.1,
                "description": "三体系列的第三部，展现了宇宙的终极命运。",
                "publication_year": 2010,
                "publisher": "重庆出版社"
            },
            {
                "title": "超新星纪元",
                "author": "刘慈欣",
                "isbn": "9787536692935",
                "genre": "科幻",
                "rating": 8.3,
                "description": "一个只有孩子的世界，探讨了人类的未来。",
                "publication_year": 2003,
                "publisher": "重庆出版社"
            },
            {
                "title": "全频带阻塞干扰",
                "author": "刘慈欣",
                "isbn": "9787536692936",
                "genre": "科幻",
                "rating": 8.4,
                "description": "一个关于电子战和人类意志的故事。",
                "publication_year": 2001,
                "publisher": "重庆出版社"
            },
            {
                "title": "白夜行",
                "author": "东野圭吾",
                "isbn": "9787544258609",
                "genre": "推理小说",
                "rating": 9.1,
                "description": "一部关于绝望与希望的推理小说，讲述了两个孩子的悲剧命运。",
                "publication_year": 1999,
                "publisher": "南海出版公司"
            },
            {
                "title": "嫌疑人X的献身",
                "author": "东野圭吾",
                "isbn": "9787544258616",
                "genre": "推理小说",
                "rating": 8.9,
                "description": "一个数学天才为了帮助邻居掩盖罪行而精心设计的完美犯罪。",
                "publication_year": 2005,
                "publisher": "南海出版公司"
            },
            {
                "title": "恶意",
                "author": "东野圭吾",
                "isbn": "9787544258617",
                "genre": "推理小说",
                "rating": 8.8,
                "description": "一个关于人性恶意的推理故事。",
                "publication_year": 1996,
                "publisher": "南海出版公司"
            },
            {
                "title": "秘密",
                "author": "东野圭吾",
                "isbn": "9787544258618",
                "genre": "推理小说",
                "rating": 8.6,
                "description": "一个关于灵魂交换的悬疑故事。",
                "publication_year": 1998,
                "publisher": "南海出版公司"
            },
            {
                "title": "挪威的森林",
                "author": "村上春树",
                "isbn": "9787532742923",
                "genre": "文学",
                "rating": 8.8,
                "description": "一部关于青春、爱情和成长的青春小说。",
                "publication_year": 1987,
                "publisher": "上海译文出版社"
            },
            {
                "title": "1Q84",
                "author": "村上春树",
                "isbn": "9787532754681",
                "genre": "文学",
                "rating": 8.5,
                "description": "一个充满悬疑和奇幻色彩的长篇小说。",
                "publication_year": 2009,
                "publisher": "南海出版公司"
            },
            {
                "title": "海边的卡夫卡",
                "author": "村上春树",
                "isbn": "9787532742924",
                "genre": "文学",
                "rating": 8.7,
                "description": "一个15岁少年的成长故事，充满超现实主义的色彩。",
                "publication_year": 2002,
                "publisher": "上海译文出版社"
            },
            {
                "title": "世界尽头与冷酷仙境",
                "author": "村上春树",
                "isbn": "9787532742925",
                "genre": "文学",
                "rating": 8.6,
                "description": "一个关于现实与虚幻交织的故事。",
                "publication_year": 1985,
                "publisher": "上海译文出版社"
            },
            {
                "title": "且听风吟",
                "author": "村上春树",
                "isbn": "9787532742926",
                "genre": "文学",
                "rating": 8.4,
                "description": "村上春树的处女作，描写了青春期的迷茫。",
                "publication_year": 1979,
                "publisher": "上海译文出版社"
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
                "title": "一桩事先张扬的凶杀案",
                "author": "加西亚·马尔克斯",
                "isbn": "9787544253996",
                "genre": "魔幻现实主义",
                "rating": 8.7,
                "description": "一个关于宿命和暴力的故事。",
                "publication_year": 1981,
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
                "title": "美丽新世界",
                "author": "阿道司·赫胥黎",
                "isbn": "9787532749521",
                "genre": "反乌托邦",
                "rating": 8.9,
                "description": "描绘了一个通过科技控制人类的未来社会。",
                "publication_year": 1932,
                "publisher": "译林出版社"
            },
            {
                "title": "我们",
                "author": "叶夫根尼·扎米亚京",
                "isbn": "9787532749522",
                "genre": "反乌托邦",
                "rating": 8.6,
                "description": "反乌托邦小说的开山之作。",
                "publication_year": 1921,
                "publisher": "译林出版社"
            },
            {
                "title": "追忆似水年华",
                "author": "马塞尔·普鲁斯特",
                "isbn": "9787532749523",
                "genre": "文学",
                "rating": 9.0,
                "description": "一部意识流小说的代表作，探讨了时间和记忆。",
                "publication_year": 1913,
                "publisher": "译林出版社"
            },
            {
                "title": "尤利西斯",
                "author": "詹姆斯·乔伊斯",
                "isbn": "9787532749524",
                "genre": "文学",
                "rating": 8.8,
                "description": "意识流小说的经典之作，描写了都柏林一天的生活。",
                "publication_year": 1922,
                "publisher": "译林出版社"
            },
            {
                "title": "等待戈多",
                "author": "塞缪尔·贝克特",
                "isbn": "9787532749525",
                "genre": "戏剧",
                "rating": 8.7,
                "description": "荒诞派戏剧的代表作，探讨了存在的意义。",
                "publication_year": 1953,
                "publisher": "人民文学出版社"
            },
            {
                "title": "存在与时间",
                "author": "马丁·海德格尔",
                "isbn": "9787100013274",
                "genre": "哲学",
                "rating": 9.0,
                "description": "存在主义哲学的经典著作，探讨了存在的意义。",
                "publication_year": 1927,
                "publisher": "商务印书馆"
            },
            {
                "title": "存在与虚无",
                "author": "让-保罗·萨特",
                "isbn": "9787100013275",
                "genre": "哲学",
                "rating": 8.9,
                "description": "存在主义哲学的重要著作，探讨了自由和责任。",
                "publication_year": 1943,
                "publisher": "商务印书馆"
            },
            {
                "title": "查拉图斯特拉如是说",
                "author": "弗里德里希·尼采",
                "isbn": "9787100013276",
                "genre": "哲学",
                "rating": 8.8,
                "description": "尼采的哲学代表作，提出了超人哲学。",
                "publication_year": 1883,
                "publisher": "商务印书馆"
            },
            {
                "title": "悲剧的诞生",
                "author": "弗里德里希·尼采",
                "isbn": "9787100013277",
                "genre": "哲学",
                "rating": 8.7,
                "description": "尼采的早期作品，探讨了艺术和人生的关系。",
                "publication_year": 1872,
                "publisher": "商务印书馆"
            },
            {
                "title": "理想国",
                "author": "柏拉图",
                "isbn": "9787100013278",
                "genre": "哲学",
                "rating": 9.1,
                "description": "柏拉图的代表作，探讨了理想的政治制度。",
                "publication_year": -380,
                "publisher": "商务印书馆"
            },
            {
                "title": "论语",
                "author": "孔子",
                "isbn": "9787100013279",
                "genre": "哲学",
                "rating": 9.3,
                "description": "儒家经典，记录了孔子及其弟子的言行。",
                "publication_year": -479,
                "publisher": "中华书局"
            },
            {
                "title": "道德经",
                "author": "老子",
                "isbn": "9787100013280",
                "genre": "哲学",
                "rating": 9.2,
                "description": "道家经典，探讨了道和德的关系。",
                "publication_year": -500,
                "publisher": "中华书局"
            },
            {
                "title": "庄子",
                "author": "庄子",
                "isbn": "9787100013281",
                "genre": "哲学",
                "rating": 9.1,
                "description": "道家经典，充满了哲学思辨和文学想象。",
                "publication_year": -300,
                "publisher": "中华书局"
            },
            {
                "title": "史记",
                "author": "司马迁",
                "isbn": "9787100013282",
                "genre": "历史",
                "rating": 9.4,
                "description": "中国第一部纪传体通史，记录了从黄帝到汉武帝的历史。",
                "publication_year": -91,
                "publisher": "中华书局"
            },
            {
                "title": "资治通鉴",
                "author": "司马光",
                "isbn": "9787100013283",
                "genre": "历史",
                "rating": 9.3,
                "description": "中国第一部编年体通史，记录了从战国到五代的历史。",
                "publication_year": 1084,
                "publisher": "中华书局"
            },
            {
                "title": "人类简史",
                "author": "尤瓦尔·赫拉利",
                "isbn": "9787508647357",
                "genre": "历史",
                "rating": 9.0,
                "description": "从认知革命到科学革命，探讨了人类历史的演进。",
                "publication_year": 2011,
                "publisher": "中信出版社"
            },
            {
                "title": "未来简史",
                "author": "尤瓦尔·赫拉利",
                "isbn": "9787508647358",
                "genre": "历史",
                "rating": 8.8,
                "description": "探讨了人类未来的可能性和挑战。",
                "publication_year": 2016,
                "publisher": "中信出版社"
            },
            {
                "title": "今日简史",
                "author": "尤瓦尔·赫拉利",
                "isbn": "9787508647359",
                "genre": "历史",
                "rating": 8.7,
                "description": "探讨了当前人类面临的重大挑战。",
                "publication_year": 2018,
                "publisher": "中信出版社"
            },
            {
                "title": "时间简史",
                "author": "斯蒂芬·霍金",
                "isbn": "9787535732309",
                "genre": "科普",
                "rating": 9.1,
                "description": "探讨了宇宙的起源、演化和未来。",
                "publication_year": 1988,
                "publisher": "湖南科学技术出版社"
            },
            {
                "title": "大设计",
                "author": "斯蒂芬·霍金",
                "isbn": "9787535732310",
                "genre": "科普",
                "rating": 8.9,
                "description": "探讨了宇宙的终极问题和科学的本质。",
                "publication_year": 2010,
                "publisher": "湖南科学技术出版社"
            },
            {
                "title": "物种起源",
                "author": "查尔斯·达尔文",
                "isbn": "9787100013284",
                "genre": "科普",
                "rating": 9.2,
                "description": "进化论的奠基之作，阐述了物种的起源和演化。",
                "publication_year": 1859,
                "publisher": "商务印书馆"
            },
            {
                "title": "梦的解析",
                "author": "西格蒙德·弗洛伊德",
                "isbn": "9787100013285",
                "genre": "心理学",
                "rating": 8.8,
                "description": "精神分析学的奠基之作，探讨了梦的心理学意义。",
                "publication_year": 1899,
                "publisher": "商务印书馆"
            },
            {
                "title": "乌合之众",
                "author": "古斯塔夫·勒庞",
                "isbn": "9787100013286",
                "genre": "心理学",
                "rating": 8.6,
                "description": "群体心理学的经典著作，探讨了群体的心理特征。",
                "publication_year": 1895,
                "publisher": "中央编译出版社"
            },
            {
                "title": "思考，快与慢",
                "author": "丹尼尔·卡尼曼",
                "isbn": "9787508633558",
                "genre": "心理学",
                "rating": 8.9,
                "description": "探讨了人类思维的两种系统：快思考和慢思考。",
                "publication_year": 2011,
                "publisher": "中信出版社"
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
                    "books": ["解忧杂货店", "白夜行", "嫌疑人X的献身"],
                    "style": "悬疑推理"
                },
                "村上春树": {
                    "genres": ["文学"],
                    "books": ["挪威的森林", "1Q84", "海边的卡夫卡"],
                    "style": "超现实主义"
                },
                "莫言": {
                    "genres": ["文学"],
                    "books": ["红高粱", "丰乳肥臀", "蛙"],
                    "style": "魔幻现实主义"
                },
                "路遥": {
                    "genres": ["文学"],
                    "books": ["平凡的世界", "人生"],
                    "style": "现实主义"
                },
                "王小波": {
                    "genres": ["文学", "杂文"],
                    "books": ["黄金时代", "沉默的大多数"],
                    "style": "黑色幽默"
                },
                "钱钟书": {
                    "genres": ["文学"],
                    "books": ["围城"],
                    "style": "讽刺文学"
                },
                "沈从文": {
                    "genres": ["文学"],
                    "books": ["边城"],
                    "style": "乡土文学"
                },
                "海明威": {
                    "genres": ["文学"],
                    "books": ["老人与海", "太阳照常升起"],
                    "style": "冰山理论"
                },
                "卡夫卡": {
                    "genres": ["文学"],
                    "books": ["变形记", "城堡"],
                    "style": "荒诞主义"
                },
                "卡勒德·胡赛尼": {
                    "genres": ["文学"],
                    "books": ["追风筝的人", "灿烂千阳"],
                    "style": "现实主义"
                },
                "安托万·德·圣埃克苏佩里": {
                    "genres": ["童话"],
                    "books": ["小王子"],
                    "style": "哲理童话"
                },
                "毛姆": {
                    "genres": ["文学"],
                    "books": ["月亮与六便士", "人性的枷锁"],
                    "style": "现实主义"
                },
                "阿尔贝·加缪": {
                    "genres": ["文学"],
                    "books": ["局外人", "鼠疫"],
                    "style": "存在主义"
                },
                "J.D.塞林格": {
                    "genres": ["文学"],
                    "books": ["麦田里的守望者"],
                    "style": "现代主义"
                },
                "F.斯科特·菲茨杰拉德": {
                    "genres": ["文学"],
                    "books": ["了不起的盖茨比"],
                    "style": "现代主义"
                },
                "哈珀·李": {
                    "genres": ["文学"],
                    "books": ["杀死一只知更鸟"],
                    "style": "现实主义"
                },
                "玛格丽特·米切尔": {
                    "genres": ["文学"],
                    "books": ["飘"],
                    "style": "历史小说"
                },
                "夏洛蒂·勃朗特": {
                    "genres": ["文学"],
                    "books": ["简·爱"],
                    "style": "现实主义"
                },
                "艾米莉·勃朗特": {
                    "genres": ["文学"],
                    "books": ["呼啸山庄"],
                    "style": "哥特式"
                },
                "简·奥斯汀": {
                    "genres": ["文学"],
                    "books": ["傲慢与偏见"],
                    "style": "现实主义"
                },
                "陀思妥耶夫斯基": {
                    "genres": ["文学"],
                    "books": ["罪与罚"],
                    "style": "心理现实主义"
                },
                "列夫·托尔斯泰": {
                    "genres": ["文学"],
                    "books": ["战争与和平", "安娜·卡列尼娜", "复活"],
                    "style": "现实主义"
                },
                "曹雪芹": {
                    "genres": ["古典文学"],
                    "books": ["红楼梦"],
                    "style": "现实主义"
                },
                "吴承恩": {
                    "genres": ["古典文学"],
                    "books": ["西游记"],
                    "style": "神魔小说"
                },
                "施耐庵": {
                    "genres": ["古典文学"],
                    "books": ["水浒传"],
                    "style": "英雄传奇"
                },
                "罗贯中": {
                    "genres": ["古典文学"],
                    "books": ["三国演义"],
                    "style": "历史演义"
                },
                "鲁迅": {
                    "genres": ["文学", "散文"],
                    "books": ["呐喊", "彷徨", "朝花夕拾"],
                    "style": "现实主义"
                },
                "巴金": {
                    "genres": ["文学"],
                    "books": ["家", "春", "秋"],
                    "style": "现实主义"
                },
                "老舍": {
                    "genres": ["文学", "戏剧"],
                    "books": ["骆驼祥子", "茶馆"],
                    "style": "现实主义"
                },
                "曹禺": {
                    "genres": ["戏剧"],
                    "books": ["雷雨"],
                    "style": "现实主义"
                },
                "茅盾": {
                    "genres": ["文学"],
                    "books": ["子夜"],
                    "style": "现实主义"
                },
                "陈忠实": {
                    "genres": ["文学"],
                    "books": ["白鹿原"],
                    "style": "现实主义"
                },
                "王安忆": {
                    "genres": ["文学"],
                    "books": ["长恨歌"],
                    "style": "现实主义"
                },
                "刘慈欣": {
                    "genres": ["科幻"],
                    "books": ["三体", "流浪地球", "球状闪电", "三体II：黑暗森林", "三体III：死神永生", "超新星纪元", "全频带阻塞干扰"],
                    "style": "硬科幻"
                },
                "东野圭吾": {
                    "genres": ["推理小说"],
                    "books": ["解忧杂货店", "白夜行", "嫌疑人X的献身", "恶意", "秘密"],
                    "style": "悬疑推理"
                },
                "村上春树": {
                    "genres": ["文学"],
                    "books": ["挪威的森林", "1Q84", "海边的卡夫卡", "世界尽头与冷酷仙境", "且听风吟"],
                    "style": "超现实主义"
                },
                "加西亚·马尔克斯": {
                    "genres": ["魔幻现实主义"],
                    "books": ["百年孤独", "霍乱时期的爱情", "一桩事先张扬的凶杀案"],
                    "style": "魔幻现实主义"
                },
                "乔治·奥威尔": {
                    "genres": ["反乌托邦"],
                    "books": ["1984", "动物农场"],
                    "style": "政治讽刺"
                },
                "阿道司·赫胥黎": {
                    "genres": ["反乌托邦"],
                    "books": ["美丽新世界"],
                    "style": "反乌托邦"
                },
                "叶夫根尼·扎米亚京": {
                    "genres": ["反乌托邦"],
                    "books": ["我们"],
                    "style": "反乌托邦"
                },
                "马塞尔·普鲁斯特": {
                    "genres": ["文学"],
                    "books": ["追忆似水年华"],
                    "style": "意识流"
                },
                "詹姆斯·乔伊斯": {
                    "genres": ["文学"],
                    "books": ["尤利西斯"],
                    "style": "意识流"
                },
                "塞缪尔·贝克特": {
                    "genres": ["戏剧"],
                    "books": ["等待戈多"],
                    "style": "荒诞派"
                },
                "马丁·海德格尔": {
                    "genres": ["哲学"],
                    "books": ["存在与时间"],
                    "style": "存在主义"
                },
                "让-保罗·萨特": {
                    "genres": ["哲学"],
                    "books": ["存在与虚无"],
                    "style": "存在主义"
                },
                "弗里德里希·尼采": {
                    "genres": ["哲学"],
                    "books": ["查拉图斯特拉如是说", "悲剧的诞生"],
                    "style": "哲学"
                },
                "柏拉图": {
                    "genres": ["哲学"],
                    "books": ["理想国"],
                    "style": "哲学"
                },
                "孔子": {
                    "genres": ["哲学"],
                    "books": ["论语"],
                    "style": "儒家"
                },
                "老子": {
                    "genres": ["哲学"],
                    "books": ["道德经"],
                    "style": "道家"
                },
                "庄子": {
                    "genres": ["哲学"],
                    "books": ["庄子"],
                    "style": "道家"
                },
                "司马迁": {
                    "genres": ["历史"],
                    "books": ["史记"],
                    "style": "史学"
                },
                "司马光": {
                    "genres": ["历史"],
                    "books": ["资治通鉴"],
                    "style": "史学"
                },
                "尤瓦尔·赫拉利": {
                    "genres": ["历史"],
                    "books": ["人类简史", "未来简史", "今日简史"],
                    "style": "通俗历史"
                },
                "斯蒂芬·霍金": {
                    "genres": ["科普"],
                    "books": ["时间简史", "大设计"],
                    "style": "科普"
                },
                "查尔斯·达尔文": {
                    "genres": ["科普"],
                    "books": ["物种起源"],
                    "style": "科学"
                },
                "西格蒙德·弗洛伊德": {
                    "genres": ["心理学"],
                    "books": ["梦的解析"],
                    "style": "精神分析"
                },
                "古斯塔夫·勒庞": {
                    "genres": ["心理学"],
                    "books": ["乌合之众"],
                    "style": "群体心理学"
                },
                "丹尼尔·卡尼曼": {
                    "genres": ["心理学"],
                    "books": ["思考，快与慢"],
                    "style": "行为经济学"
                }
            },
            "genres": {
                "科幻": {
                    "authors": ["刘慈欣"],
                    "similar_genres": ["魔幻现实主义", "反乌托邦", "文学", "科普"]
                },
                "文学": {
                    "authors": ["余华", "村上春树", "莫言", "路遥", "王小波", "钱钟书", "沈从文", "海明威", "卡夫卡", "卡勒德·胡赛尼", "毛姆", "阿尔贝·加缪", "J.D.塞林格", "F.斯科特·菲茨杰拉德", "哈珀·李", "玛格丽特·米切尔", "夏洛蒂·勃朗特", "艾米莉·勃朗特", "简·奥斯汀", "陀思妥耶夫斯基", "列夫·托尔斯泰", "鲁迅", "巴金", "老舍", "茅盾", "陈忠实", "王安忆", "马塞尔·普鲁斯特", "詹姆斯·乔伊斯"],
                    "similar_genres": ["魔幻现实主义", "推理小说", "童话", "古典文学", "散文", "戏剧"]
                },
                "古典文学": {
                    "authors": ["曹雪芹", "吴承恩", "施耐庵", "罗贯中"],
                    "similar_genres": ["文学", "历史"]
                },
                "散文": {
                    "authors": ["鲁迅", "王小波"],
                    "similar_genres": ["文学"]
                },
                "戏剧": {
                    "authors": ["老舍", "曹禺", "塞缪尔·贝克特"],
                    "similar_genres": ["文学"]
                },
                "魔幻现实主义": {
                    "authors": ["加西亚·马尔克斯", "莫言"],
                    "similar_genres": ["文学", "科幻", "古典文学"]
                },
                "反乌托邦": {
                    "authors": ["乔治·奥威尔", "阿道司·赫胥黎", "叶夫根尼·扎米亚京"],
                    "similar_genres": ["科幻", "文学"]
                },
                "推理小说": {
                    "authors": ["东野圭吾"],
                    "similar_genres": ["文学"]
                },
                "童话": {
                    "authors": ["安托万·德·圣埃克苏佩里"],
                    "similar_genres": ["文学"]
                },
                "杂文": {
                    "authors": ["王小波"],
                    "similar_genres": ["文学", "散文"]
                },
                "哲学": {
                    "authors": ["马丁·海德格尔", "让-保罗·萨特", "弗里德里希·尼采", "柏拉图", "孔子", "老子", "庄子"],
                    "similar_genres": ["文学", "历史"]
                },
                "历史": {
                    "authors": ["司马迁", "司马光", "尤瓦尔·赫拉利"],
                    "similar_genres": ["文学", "古典文学", "哲学"]
                },
                "科普": {
                    "authors": ["斯蒂芬·霍金", "查尔斯·达尔文"],
                    "similar_genres": ["科幻", "哲学"]
                },
                "心理学": {
                    "authors": ["西格蒙德·弗洛伊德", "古斯塔夫·勒庞", "丹尼尔·卡尼曼"],
                    "similar_genres": ["哲学", "文学"]
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