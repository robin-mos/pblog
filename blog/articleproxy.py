#coding=utf-8
from django.shortcuts import render
import blog.article

######################
# License: LiXiangping
# Version: V1.0
# Release: 1.0
# Author: LiXiangping
# Date: 2018/02/26
# Email: 752070569@qq.com
# Description: 根据查询信息返回页面
######################

class ArticleManager:
    def Home(request):
        postlist = blog.article.Home(request)
        return render(request, 'home.html', {'post_list': postlist})

    def Detail(request, id):
        post = blog.article.Detail(request, id)
        return render(request, 'post.html', {'post': post})
