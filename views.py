
#处理函数（控制器）的编写， 需要返回一个httpresponse类的实例
# 送回给客户的快递包裹
# from django.http import HttpResponse
# def index(request): # request 是个 对象
#     return HttpResponse("Hello World!@")

from django.shortcuts import render

def index(request):
     return render(request,"index.html")