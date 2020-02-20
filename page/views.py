from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Post

def home(request):
    posts = Post.objects.all()
    return render(request,'home.html',{'posts':posts})
#요청이 들어왔을 때 home을 보여주는 코드임.

def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request,'detail.html',{'post':post})

def new(request):
    if request.method == 'POST':
        post = Post()
        post.author = request.user
        post.title = request.POST['title']
        post.content = request.POST['content']
        post.pub_date = timezone.datetime.now()
        post.save()
        return redirect('/detail/'+str(post.id))
    else:
        return render(request,'new.html')
