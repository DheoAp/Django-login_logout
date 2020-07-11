from django.contrib import admin
from django.urls import path
from django.contrib.auth.decorators import login_required

from accounts.views import index, pageAdmin, LoginPage, LogoutPage

urlpatterns = [
    path('', index, name='index'),
    path('PageAdmin',pageAdmin, name='page-admin'),

    path('login',LoginPage, name='login'),
    path('logout',LogoutPage, name='logout'),

    
    path('admin/', admin.site.urls),
]
