from django.shortcuts import render, get_object_or_404
from . models import Blog

def all_blogs(request):
    blogs_w = Blog.objects.count
    blogs = Blog.objects.order_by('-date')[:5]
    return render(request, 'blog/all_blogs.html', {'blogs':blogs, 'blogs_w':blogs_w})

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html',{'blog':blog})