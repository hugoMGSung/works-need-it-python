from tkinter import Widget
from django import forms
from .models import Post

class PostForm(forms.ModelForm): 
    class Meta:
        model = Post    # 사용할 모델
        fields = ['title', 'content', 'writer']  # Post에서 사용할 속성
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'writer': forms.TextInput(attrs={'class': 'form-control'})            
        }
        labels = {
            'title': '제목',
            'content': '내용',
            'writer': '글쓴이'
        }  