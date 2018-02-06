#coding=utf-8
from __future__ import unicode_literals
from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(u'博客标题',max_length=100)
    category = models.CharField(u'博客标签',max_length=50,blank=True)
    pub_date = models.DateTimeField(u'发布日期',auto_now_add=True,editable=True)
    update_time = models.DateTimeField(u'更新日期',auto_now_add=True,null=True)
    content = models.TextField(blank=True,null=True)

    def __unicode__(self):
        return self.title

    #内部模型
    class Meta:
        ordering=['-pub_date']      #降序排列
        verbose_name = '文章'
        verbose_name_plural='文章'