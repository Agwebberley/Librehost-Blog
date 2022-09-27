from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Blog, Comment


# Create your forms here.

class NewUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ("username", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		if commit:
			user.save()
		return user

class BlogForm(forms.ModelForm):
	class Meta:
		model = Blog
		fields = ['title', 'body']
		fields_required = ['title', 'body']
		
	def save(self, commit=True):
		
		blog = super(BlogForm, self).save(commit=False)
		if commit:
			blog.save()
		return blog

class CommentForm(forms.ModelForm):
    comment = forms.CharField(
        label='',
        widget=forms.Textarea(
            attrs={'rows': '3',
                   'placeholder': 'Say Something...'}
        ))
    class Meta:
        model = Comment
        fields = ['comment']
