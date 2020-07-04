from django.contrib import admin
from django.urls import path
from django.contrib.auth.decorators import login_required

from accounts.views import Index, PageAdmin, LoginPage, LogoutPage

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('PageAdmin',login_required( PageAdmin.as_view()), name='page-admin'),

    path('login',LoginPage, name='login'),
    path('logout',LogoutPage, name='logout'),

    
    path('admin/', admin.site.urls),
]
