from django.shortcuts import render
from .models import Post, Comment

# Create your views here.
def post_list(request):
    post = Post.objects.all()
    comment = Comment.objects.all()
    
    context = {
        "posts": post,
        "comments" : comment
    }
    return render(request, 'post_list.html', context)

def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    print(post)
    context = {
        "post": post
    }
    return render(request, "post_detail.html", context)

def post_add(request):
    return render(request, "post_add.html")