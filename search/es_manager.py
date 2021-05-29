from elasticsearch import Elasticsearch
es = Elasticsearch()

def query_es(query):
    res = es.search(index="web_data", body={ "query" : { "match" : { "content" : query } } } )
    res = [item for item in res['hits']['hits']]
    final_res = []
    for item in res:
        data = item['_source']
        data['score'] = item['_score']
        if len(data['content']) > 600:
            data['content'] = data['content'][:600]+" ..."
        final_res.append(data)
    return final_res
