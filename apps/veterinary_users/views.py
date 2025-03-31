from django.shortcuts import render
from django.http import HttpResponse

def users_home(request):
    return render(request, 'veterinary_users/users_home.html')
