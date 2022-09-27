from django.shortcuts import render, redirect
from .models import Blog, Comment
from django.views.generic import ListView, DetailView
from .forms import NewUserForm, BlogForm, CommentForm
from django.contrib.auth import login, authenticate, logout 
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm 
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
# Create your views here.

# Home view for blog
class HomeView(ListView):
    model = Blog
    template_name = 'home.html'

class BlogDetailView(DetailView):
    def get(self, request, pk, *args, **kwargs):
        post = Blog.objects.get(pk=pk)
        form = CommentForm()
        comments = Comment.objects.filter(post=post).order_by('-created_on')
        context = {
            'post': post,
            'form': form,
            'comments': comments,
        }
        return render(request, 'social/post_detail.html', context)
    def post(self, request, pk, *args, **kwargs):
        post = Blog.objects.get(pk=pk)
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.author = request.user
            new_comment.post = post
            new_comment.save()
        
        comments = Comment.objects.filter(post=post).order_by('-created_on')
        context = {
            'post': post,
            'form': form,
            'comments': comments,
        }
        return render(request, 'social/post_detail.html', context)


class PostEditView(UpdateView):
    model = Blog
    fields = ['body']
    template_name = 'post_edit.html'
    
    def get_success_url(self):
        slug = self.kwargs['slug']
        return reverse_lazy('blog_detail', kwargs={'slug': slug})

class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'comment_delete.html'
    def get_success_url(self):
        slug = self.kwargs['slug']
        return reverse_lazy('blog_detail', kwargs={'slug': slug})
    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author



def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("home")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="register.html", context={"register_form":form})


def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("home")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("home")


def publishBlog(request):
	if request.method == "POST":
		if request.user.is_authenticated:
			form = BlogForm(request.POST)
			if form.is_valid():
				blog = form.save(commit=False)
				blog.author = request.user
				blog.save()
				return redirect("home")
			else:
				messages.error(request, "Your Post Is Invalid.")
	else:
		form = BlogForm()
	return render(request, 'post.html', {'form': form})

def delete_post(request, slug):
    post = Blog.objects.filter(slug=slug)
    post.delete()
    return redirect('/')
