from .models import Post
from django import forms
from django.contrib.auth.models import User


class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('post_img','caption','comment',)


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name','last_name','email')
