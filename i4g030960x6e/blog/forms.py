from dataclasses import field
from django import forms

from . models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        field = ["__all__"]