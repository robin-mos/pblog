#coding=utf-8
from django.contrib import admin
from blog.models import Article

# Register your models here.
# 注册模型到管理账户
# Author: LiXiangping
# Date: 2018/02/24
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','pub_date')

admin.site.register(Article,ArticleAdmin)
