from django import forms
from MebukiTechapp.models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = (
            'comment',
        )