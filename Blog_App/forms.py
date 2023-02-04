from django import forms
from Blog_App.models import Comment
from captcha.fields import CaptchaField


class CommentForm(forms.ModelForm):
    #captcha = CaptchaField()

    class Meta:
        model = Comment
        fields = ['post','name', 'email','subject','message']