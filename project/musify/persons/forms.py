from django import forms
from django.contrib.auth import authenticate,login,logout,get_user_model

User=get_user_model()

class Login_form(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(Login_form, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'full-width has-padding has-border'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['password'].widget.attrs['class'] = 'full-width has-padding has-border'
        self.fields['password'].widget.attrs['placeholder'] = 'Password'


    def clean(self,*args,**kwargs):
        username=self.cleaned_data.get('username')
        password=self.cleaned_data.get('password')
        user=authenticate(username=username,password=password)

        if not user:
            raise forms.ValidationError("Invalid username or password")

        return super(Login_form,self).clean(*args,**kwargs)


class Registration_form(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','email','password']

    def __init__(self, *args, **kwargs):
        super(Registration_form, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'full-width has-padding has-border'
        self.fields['email'].widget.attrs['class'] = 'full-width has-padding has-border'
        self.fields['password'].widget.attrs['class'] = 'full-width has-padding has-border'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['email'].widget.attrs['placeholder'] = 'E-mail'
        self.fields['password'].widget.attrs['placeholder'] = 'Password'

    def clean_email(self,*args,**kwargs):
        email=self.cleaned_data.get('email')
        instances=User.objects.filter(email=email)

        if instances.count():
            raise forms.ValidationError("A user already exists with that email")

        return super(Registration_form,self).clean(*args,**kwargs)
