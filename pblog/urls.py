"""pblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import include, url
from DjangoUeditor import urls as djud_urls
from django.conf import settings
import blog.views
########################
# Version V1.0
# Release 1.0
# Author: LiXiangping
# Email: 752070569@qq.com
# Date: 2018/02/24
# Description:过滤请求地址
#########################
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^ueditor/',include(djud_urls)),
    url(r'^test/',blog.views.test,name='blog test'),
    url(r'^detail/(?P<id>\d+)/$',blog.views.Detail,name="blog_detail"),
    url(r'^home/',blog.views.Home,name="blog_home"),
]


###############
# Version V1.0
# Release 1.0
# Description: 让django访问百度开发的DjangoUeditor模块
###############
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
