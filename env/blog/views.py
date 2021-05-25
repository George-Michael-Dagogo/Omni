from django.shortcuts import render,redirect
from .models import Post, Comment
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.forms import inlineformset_factory
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm, PasswordChangeForm 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import *
from .forms import CommentForm, CreateUserForm

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return redirect('login')


        context = {'form':form}
        return render(request, 'register.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password =request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

# Create your views here.
class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('password_success')

def password_success(request):
    return render (request, "password_success.html", {})

class BlogCommentView(CreateView, LoginRequiredMixin):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    model = Comment
    form_class = CommentForm
    template_name= 'add_comment.html'
    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

    success_url = reverse_lazy('home')

    #fields = ['post','author','body']

class BlogListView(ListView, LoginRequiredMixin):
    login_url = 'login/'
    redirect_field_name = 'redirect_to'
    model = Post
    template_name = 'home.html'

class BlogDetailView(DetailView, LoginRequiredMixin):
    login_url = 'login/'
    redirect_field_name = 'redirect_to'
    model = Post
    template_name = 'post_detail.html'

class BlogCreateView(CreateView, LoginRequiredMixin):
    login_url = 'login/'
    redirect_field_name = 'redirect_to'
    model = Post
    template_name= 'post_new.html'
    fields = ['title','author','body']

class BlogUpdateView(UpdateView, LoginRequiredMixin):
    login_url = 'login/'
    redirect_field_name = 'redirect_to'
    model = Post
    template_name = 'post_edit.html'
    fields = ['title','body']
class BlogDeleteView(DeleteView, LoginRequiredMixin):
    login_url = 'login/'
    redirect_field_name = 'redirect_to'
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')