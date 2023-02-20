from django import forms 
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment','user', 'book')
        
        widgets ={
        'Comment': forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Текст комментария'})
        }
    
