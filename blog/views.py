from django.shortcuts import render
from .models import BlogAplication

def all_blog(request):
    return render(request, 'blog/all_blog.html')
    projects = BlogAplication.objects.all()
    return render(request,"blog/all_blog.html", {'projects':projects})
