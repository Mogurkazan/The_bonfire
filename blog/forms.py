# blog/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Post, Comment, CustomUser

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'keywords', 'content']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    nickname = forms.CharField(max_length=30, required=True)

    class Meta:
        model = CustomUser
        fields = ('email', 'nickname', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.nickname = self.cleaned_data['nickname']
        if commit:
            user.save()
        return user
