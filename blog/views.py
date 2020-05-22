from django.shortcuts import render, get_object_or_404
from .models import BlogAplication

def all_blogs(request):

    blogs = BlogAplication.objects.order_by('-created_date')[:5]
    return render(request,"blog/all_blog.html", {'blogs':blogs})

def detail(request, blog_id):
    blog = get_object_or_404(BlogAplication, pk=blog_id)    #usado para mostrar varios valores
    return render(request, 'blog/detail.html', {'blog':blog}) # e caso nao exista ele envia um erro 404 dizendo que a pagina nao existe
