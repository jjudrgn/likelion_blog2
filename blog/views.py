from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog

# Create your views here.

def home(request):
    blogs = Blog.objects    # 쿼리셋 # 메소드
    return render(request, 'home.html', {'blogs' : blogs})

    # 쿼리셋과 메소드의 형식
    # 모델.쿼리셋(objects).메소드
def test(request):
    blogs = Blog.objects    # 쿼리셋 # 메소드
    return render(request, 'test.html', {'blogs' : blogs})

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'detail.html', {'blog':blog_detail})

def newpost(request): #newpost.html을 띄어주는 함수
    return render(request, 'newpost.html')

def create(requset):        #입력받은 내용을 데이터베이스에 넣어주는 함수
    blog = Blog()
    blog.title = requset.GET['title']
    blog.body = requset.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/'+str(blog.id))
    # 새로 페이지를 실행

