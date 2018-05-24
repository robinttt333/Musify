from django.forms import forms,ModelForm
from mediumeditor.widgets import MediumEditorTextarea
from .models import Post
class PostForm(ModelForm):
    class Meta:
        model=Post
        fields=['author','title','artist','lyrics','content','tags',]
        widgets = {
            'content': MediumEditorTextarea(),
        }