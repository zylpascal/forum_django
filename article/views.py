from django.shortcuts import render
from block.models import Block
from .models import Article

def article_lists(request, block_id):
    block_id = int(block_id) # block_id is string when feed in
    block = Block.objects.get(id=block_id)
    article_objs = Article.objects.filter(block=block,status=0).order_by("-id")
    return render(request,"article_list.html", {"articles": article_objs, "b":block})

def creat_View(request, block_id):
    return render(request, "creatPost.html")

