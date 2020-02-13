from django.shortcuts import render, get_object_or_404
from .models import Post

def home(request):
    posts = Post.objects.all()
    return render(request,'home.html',{'posts':posts})
#요청이 들어왔을 때 home을 보여주는 코드임.

def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request,'detail.html',{'post':post})