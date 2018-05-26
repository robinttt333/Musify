from django.forms import forms,ModelForm
from .models import Post
from pagedown.widgets import PagedownWidget
from django.forms import forms
from mediumeditor.widgets import MediumEditorTextarea

class PostForm(ModelForm):
    class Meta:
        model=Post
        fields=['title','lyrics','artist','image','content',]

        widgets = {
            'content': PagedownWidget(show_preview=False),
            'lyrics':MediumEditorTextarea()
        }
    #This function makes the lyrics field inside the modal form optional
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['lyrics'].required = False
