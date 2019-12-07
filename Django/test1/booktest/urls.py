from django.conf.urls import url
from booktest import views

# 严格匹配开头结尾

urlpatterns = [
    #通过url函数设置url路由配置项
    url(r'^index$',views.index),  #建立/index和视图index之间的关系
    url(r'^index2$', views.index2),  # 建立/index和视图index之间的关系
    url(r'^books$',views.show_books), #显示图书信息
    url(r'^books/(\d+)$',views.detail),  #显示英雄信息
    url(r'^login$',views.login,),  #显示登录页面
    url(r'^login_check',views.login_check),# 用户登录校验
]