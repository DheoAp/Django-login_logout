from django.views.generic import TemplateView
from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.contrib import messages # untuk pesan error atau lainnya
# Create your views here.
from .decorators import unauthenticated_user

@unauthenticated_user
def index(request):
    return render (request, 'user/index.html')

@login_required(login_url='login')
def pageAdmin(request):
    return render(request,'user/admin.html')

@unauthenticated_user # jika sudah masuk ke halaman admin makan tidak bisa masuk page login, harus logout dulu
def LoginPage(request):

    if request.method == 'POST':
        username_ = request.POST.get('username')
        password_ = request.POST.get('password')

        user = authenticate(request, username=username_, password=password_)

        if user is not None:
            login(request, user)
            return redirect('page-admin')
        else:
            messages.info(request,'Username or Password is incorrect')

    context = {}
    return render(request, 'user/login.html', context)

def LogoutPage(request) :
    logout(request)
    return redirect('login')