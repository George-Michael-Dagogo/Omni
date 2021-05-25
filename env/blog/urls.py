from django.contrib.auth.forms import PasswordChangeForm
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import BlogListView,BlogDetailView,BlogCreateView,BlogUpdateView,BlogDeleteView,BlogCommentView,PasswordsChangeView
from . import views 

urlpatterns = [
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('password/', PasswordsChangeView.as_view(template_name='change_password.html'), name = "change_password"),
    path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/edit/', BlogUpdateView.as_view(), name='post_edit'),
    path('post/new/', BlogCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name = 'post_detail'),
    path('',BlogListView.as_view(),name='home'),
    path('post/<int:pk>/comments/', BlogCommentView.as_view(), name='add_comment'),
    path('password_success', views.password_success, name = "password_success"),

]
  