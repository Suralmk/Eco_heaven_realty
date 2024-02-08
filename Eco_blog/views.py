from django.shortcuts import render
from django.http import HttpResponse
from . models import Blog
# Create your views here.


def blog(request):
    blogs = Blog.objects.all().latest()

    context = {
        "blogs" : blogs
    }
    return render(request, "Eco_blog/blogs.html", context)

def eco_blog_detail(request, blogname, id):
    blog =Blog.objects.filter(id=id).first()
    re_blog = []
    recent_blogs = Blog.objects.all()
    for recent_blog in recent_blogs:
        if recent_blog.id != id:
            re_blog.append(recent_blog)
        
    
    print(recent_blogs)
    context = {
            "blog" : blog,
            "recent_blogs" : re_blog
           
        }
    return render(request, "Eco_blog/blog_detail.html", context)