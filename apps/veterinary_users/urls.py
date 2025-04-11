from django.urls import path
from . import views

urlpatterns = [
    path('', views.users_home, name='users_home'),
    path('user/<str:username>/', views.user_detail_by_username, name='user_detail'),
]
