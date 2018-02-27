from django.shortcuts import render
from django.http import HttpResponse
import datetime
from blog.articleproxy import ArticleManager
from django.http import Http404

# Create your views here.
##############
# Version: V1.0
# Release: 1.0
# Author: LiXiangping
# Email: 752070569@qq.com
# Date: 2018/02/24
# Description: 返回显示内容
##############

def test(request):
    return render(request,'test.html',{'current_time': datetime.datetime.now()})

def Home(request):
    return ArticleManager.Home(request)

def Detail(request,id):
    return ArticleManager.Detail(request,id)
