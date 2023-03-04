from django.shortcuts import render
import json
from py2neo import *
from django.http import JsonResponse

graph=Graph("http://localhost:7474", auth=("neo4j", "123456"))
matcher=NodeMatcher(graph)

def search_one(value):
    #定义data数组存储节点信息
    data=[]
    #定义links数组存储关系信息
    links=[]

    node=matcher.match('paper',title=value).first()
    print(node)
    return node




def search_paper(request):
    if request.method=='POST':
        node_name=request.POST.get('node')
        search_neo4j_data=search_one(node_name)
        dict={}
        dict['abs']=search_neo4j_data
        return JsonResponse(dict)
# Create your views here.
