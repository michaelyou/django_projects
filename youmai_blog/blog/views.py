#encoding=UTF-8
from django.shortcuts import render
from blog.models import BlogPost 

# Create your views here.

def archive(request):
    posts = BlogPost.objects.all()  #获取数据库里的所有BlogPost对象
    context = {}
    context['posts'] = posts
    return render(request, 'archive.html', context)
    
