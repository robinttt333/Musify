from django.forms import forms,ModelForm
from .models import Post
from froala_editor.widgets import FroalaEditor
from django.forms import forms
class PostForm(ModelForm):
    class Meta:
        model=Post
        fields=['title','lyrics','artist','image','content','tags',]

        widgets = {
            'content': FroalaEditor(theme='dark')
        }
    #This function makes the lyrics field inside the modal form optional
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['lyrics'].required = False
        self.fields['tags'].required = False