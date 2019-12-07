from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader,RequestContext
from booktest.models import BookInfo  #导入图书模型类
from django.shortcuts import redirect
# Create your views here.
# 1.定义视图函数，httpRequest
# 2.进行url配置，建立url地址和视图的对应关系
# http://127.0.0.1:8000/index
def index(request):
    '''首页'''
    return render(request,'booktest/index.html')


def index2(request):
    # 进行处理，和M和T进行交互
    return HttpResponse('老铁666')

def show_books(request):
    '''显示图书的信息'''
    # 1.通过M查找图书表中的数据
    books = BookInfo.objects.all()
    # 2.使用模板
    return render(request,'booktest/show_books.html',
                  {'books':books})

def detail(request,bid):
    '''查询图书关联的英雄信息'''
    # 1.根据bid查询图书信息
    book = BookInfo.objects.get(id=bid)
    # 2.查询和book关联的英雄信息
    heros = book.heroinfo_set.all()
    # 3.使用模板
    return render(request,'booktest/detail.html',
                  {'book': book,'heros':heros})

def login(request):
    # 显示登录页面
    if 'username' in request.COOKIES:
        username = request.COOKIES['username']
    else:
        username = ''
    return render(request , 'booktest/login.html',{'username':username})

def login_check(request):
    # 登录校验视图
    # 1.获取提交的用户名和密码
    username = request.POST.get('username')
    password = request.POST.get('password')
    remember = request.POST.get('remember')
    print(remember)
    # 2.进行登录的校验
    if username == '123' and password == '123':
        return redirect('/index')
        if remember == 'on':
            response.set_cookie('username',username,max_age=7*24*3600)
    else:
        return redirect('/login')
    # 3.进行返回的应答
