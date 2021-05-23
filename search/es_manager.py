from elasticsearch import Elasticsearch
es = Elasticsearch()

def query_es(query):
    res = es.search(index="web-data", body={"query":{"match":{"content":query}}})
    res = [item for item in res['hits']['hits']]
    return res
