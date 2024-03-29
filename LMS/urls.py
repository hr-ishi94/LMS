"""
URL configuration for LMS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import user_login

urlpatterns = [
    path('admin/', admin.site.urls),

    path('',include('home.urls')),
    path('accounts/',include('django.contrib.auth.urls')),
    path('accounts/register/',user_login.register,name='register'),
    path('Do_login/',user_login.do_login,name='do_login'),
    path('logout/',user_login.logout_user,name='logout_user'),
    path('accounts/profile/',user_login.profile_view,name='profile_view'),
    path('accounts/profile/update/',user_login.profile_update,name='profile_update'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
