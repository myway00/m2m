from django import forms
from .models import Content, Comment #import는 admin에서도 폼에서도 꼭

class ContentForm(forms.ModelForm):
    class Meta:
        model = Content
        fields = ['title','body']

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=["text"]