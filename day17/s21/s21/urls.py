"""s21 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from app01 import views
urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    # 关于用户的url
    url(r'^login', views.login),
    url(r'^register_user/', views.register_user),
    url(r'^show_user', views.show_user),
    url(r'^del_user', views.del_user),
    url(r'^edit_user', views.edit_user),
    url(r'^add_user', views.add_user),
    url(r'^logout',views.logout),
    # 关于主机管理的url
    url(r'^show_host/$',views.show_host),
    # 添加主机
    url(r'^add_host/$',views.add_host, name="add_host"),
    # 编辑主机
    url(r'^edit_host/(?P<pk>\d+)$',views.edit_host,name="edit_host"),
    # 删除主机
    url(r'^del_host/(?P<pk>\d+)$', views.del_host, name="del_host"),






]
