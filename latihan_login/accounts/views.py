from django.views.generic import TemplateView
from django.shortcuts import render, redirect


from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class Index(TemplateView):
    template_name = 'user/index.html'


class PageAdmin(LoginRequiredMixin,TemplateView):
    template_name = 'user/admin.html'


def LoginPage(request):

    if request.method == 'POST':
        username_ = request.POST.get('username')
        password_ = request.POST.get('password')

        user = authenticate(request, username=username_, password=password_)

        if user is not None:
            login(request, user)
            return redirect('page-admin')
        else:
            message.info(request,'Username or Password is incorrect')

    context = {}
    return render(request, 'user/login.html', context)

def LogoutPage(request) :
    logout(request)
    return redirect('login')