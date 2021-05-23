from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .es_manager import query_es
from .stop_words import stop_words

@api_view(['GET'])
def search(request, query):
    parsed_query = query.split(' ')
    filtered_query = []

    for word in parsed_query:
        if word not in stop_words:
            filtered_query.append(word)

    joined_filtered_query = ""
    for item in filtered_query:
        joined_filtered_query += item
    res = query_es(joined_filtered_query)
    original_res = query_es(query)
    return Response(res+original_res)


@api_view(['GET'])
def mock_search(request, query):
    print("query -> ", query)
    mock_response = [{'url':'https://www.google.com', 'content':'google search'}, {'url': 'https://www.wikipedia.com', 'content':'wikipedia free encyclopedia'}]
    return Response(mock_response)
