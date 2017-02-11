from django import forms

from .models import Post, Comment


from django.forms import ModelForm

# for post text box
class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

#for comment text box
class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)
