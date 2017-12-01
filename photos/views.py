from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import NewPostForm,UserForm
from django.db import transaction



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

            return redirect('index')

    else:
        form = NewPostForm()

    return render(request,'all-photos/new_post.html',{"form":form})


@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, ('Your profile was successfully updated!'))
            return redirect('profile')
        else:
            messages.error(request, ('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'all-photos/edit_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })
