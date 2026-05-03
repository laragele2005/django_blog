from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Blog, Category
# Create your views here.


def post_by_category(request, category_id):
    # Fetch the posts that belongs to the category id
    posts = Blog.objects.filter(category_id=category_id, status="Published")
    # Try except blog when the category number does not exist, it will redirect to home page
    # try:
    #     category = Category.objects.get(pk=category_id)
    # except: 
    #     return redirect('home')
    
    category= get_object_or_404(Category,pk=category_id)
    
    context = {
        'posts':posts,
        'category':category
    }
    return render(request, 'posts_by_category.html', context)