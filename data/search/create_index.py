from elasticsearch import Elasticsearch
import time

es =  Elasticsearch(['127.0.0.1'], scheme="http", port=9200)
# 初始化索引的Mappings设置，三个字段，新闻标题，新闻内容，创建时间。
index_mappings = {
    "mappings": {
        "news": {
            "properties": {
                "title": {
                    "type": "text",
                    "analyzer": "ik_max_word",
                    "search_analyzer": "ik_max_word"
                },
                "content": {
                    "type": "text",
                    "analyzer": "ik_max_word",
                    "search_analyzer": "ik_max_word"
                }
            }
        }
    }
}

es.indices.delete(index='news_index', ignore=[400, 404])
es.indices.create(index='news_index', body=index_mappings, ignore=400)

datas = [
    {
        'title': '美国留给伊拉克的是个烂摊子吗',
        'url': 'http://view.news.qq.com/zt2011/usa_iraq/index.htm',
        'content': '2011-12-16'
    },
    {
        'title': '公安部：各地校车将享最高路权',
        'url': 'http://www.chinanews.com/gn/2011/12-16/3536077.shtml',
        'content': '2011-12-16'
    },
    {
        'title': '中韩渔警冲突调查：韩警平均每天扣1艘中国渔船',
        'url': 'https://news.qq.com/a/20111216/001044.htm',
        'content': '2011-12-17'
    },
    {
        'title': '中国驻洛杉矶领事馆遭亚裔男子枪击 嫌犯已自首',
        'url': 'http://news.ifeng.com/world/detail_2011_12/16/11372558_0.shtml',
        'content': '2011-12-18'
    }
]

for data in datas:
    es.index(index='news_index', doc_type='news', body=data)


result = es.search(index='company')
print(result)


dsl = {
    'query': {
        'multi_match': {
            'query': '中国',
            "fields": ["title", "content"]
        }
    },
    "highlight": {
        "fields": {
            "content": {},
            "title": {}
        }
    }
}

# 刚写的数据查不出来
es1 = Elasticsearch(['127.0.0.1'], scheme="http", port=9200)
datList = es1.search(index="news_index", body=dsl)
print(datList)
