from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import register, CustomLoginView, admin_users

urlpatterns = [
    path('', views.users_home, name='users_home'),
    path('user/<str:username>/', views.user_detail_by_username, name='user_detail'),
    path('user/<str:username>/edit/', views.user_edit, name='user_edit'),
    path('user/<str:username>/delete/', views.user_delete, name='user_delete'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', register, name='register'),
    path('admin', admin_users, name='admin_users'),
]
