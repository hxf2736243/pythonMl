from elasticsearch import Elasticsearch
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

es1 = Elasticsearch(['127.0.0.1'], scheme="http", port=9200)
datList = es1.search(index="news_index", body=dsl)
print(datList)
