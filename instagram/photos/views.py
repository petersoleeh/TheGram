from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import NewPostForm



# Create your views here
@login_required(login_url='/accounts/login/')
def index(request):
    post = Post.objects.all()
    current_user = request.user
    if request.method == 'POST':
        form = NewPostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()

    else:
        form = NewPostForm()

    return render(request,'index.html',{"form":form,"post":post})


def profile(request):
    post = Post.objects.all()
    return render(request,'all-photos/profile.html',{"post":post})


def new_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewPostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()

    else:
        form = NewPostForm()

    return render(request,'all-photos/new_post.html',{"form":form})
