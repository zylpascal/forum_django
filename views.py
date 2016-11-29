# 处理函数（控制器）的编写， 需要返回一个httpresponse类的实例
# 送回给客户的快递包裹
# from django.http import HttpResponse
# def index(request): # request 是个 对象
#     return HttpResponse("Hello World!@")

from django.shortcuts import render
from block.models import Block

# block_infos is a queryset object
# id is default added by django
#block_infos = Block.objects.all().order_by("-id")
block_infos = Block.objects.all().filter(status=0).order_by("-id")
# wehn views changes, need manually restart server

def index(request):
    # block_infos = [{"name": "运维专区", "desc": "运维学习讨论区", "manager": "admin"},
    #                {"name": "Django专区", "desc": "Django学习讨论区", "manager": "admin"},
    #                {"name": "部落建设", "desc": "有关部落建设的事宜", "manager": "admin"}]
    return render(request, "index.html", {"blocks": block_infos})
