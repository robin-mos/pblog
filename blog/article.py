#coding=utf-8

from blog.models import Article
from django.shortcuts import render
from django.http import Http404

######################
# Version: V1.0
# Release: 1.0
# Author: LiXiangping
# Date: 2018/02/26
# Email: 752070569@qq.com
# Description: 查询博客文章信息
######################

# Description: 查询数据库全部信息
# Return: 返回查询的结果
def Home(request):
    postlist = Article.objects.all()
    return postlist


# Description: 根据id查询数据库信息
# Return: 返回查询结果
def Detail(request,id):
    try:
        post = Article.objects.get(id=str(id))
    except Article.DoesNotExist:
        raise Http404
    return post
