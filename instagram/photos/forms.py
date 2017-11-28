from .models import Post,User
from django import forms


class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('post_img','caption','comment',)
