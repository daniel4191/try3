from django.shortcuts import render, redirect
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
    
    context = {
        "post": post
    }
    
    if request.method == "POST":
        comment = request.POST.get("comment","").strip()
        if comment:
            Comment.objects.create(
                post = post,
                comment = comment
            )
            return redirect(request.path)
        else:
            pass
    return render(request, "post_detail.html", context)

def post_add(request):
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']
        writer = request.POST['writer']
        
        post = Post.objects.create(
            title=title,
            writer=writer,
            content=content
        )
        return redirect(f"/posts/{post.id}")
    return render(request, "post_add.html")