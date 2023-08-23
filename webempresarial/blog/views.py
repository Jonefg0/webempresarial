from django.shortcuts import render, get_object_or_404
from .models import Post, Category

# Create your views here.

def blog(request):
    Posts = Post.objects.all()
    return render(request, "blog/blog.html",{'posts':Posts})

def category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    #posts = Post.objects.filter(categories=category)
    #category = Category.objects.get(id=category_id) # va a traer la categoria con todos su parametros y que contenga a el id.
    return render(request, "blog/category.html",{'category':category})