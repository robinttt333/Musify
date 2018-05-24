from django.forms import forms,ModelForm

from .models import Post
class PostForm(ModelForm):
    class Meta:
        model=Post
        fields=['author','title','artist','lyrics','content','tags',]