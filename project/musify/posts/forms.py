from django.forms import forms,ModelForm
from mediumeditor.widgets import MediumEditorTextarea
from django.forms.widgets import TextInput
from .models import Post
from django.forms import forms
class PostForm(ModelForm):
    class Meta:
        model=Post
        fields=['title','lyrics','artist','content','tags',]

        widgets = {
            'content': MediumEditorTextarea(),
        }

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['lyrics'].required = False