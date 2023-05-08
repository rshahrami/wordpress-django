"""eittaweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from post.views import *
from mokeb.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.urls import re_path as url
from django.views.static import serve
from homepage.views import *
from uploadimage.views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', HomePageViews, name='homepage'),
    path('home/', PostViews, name='home'),
    path('UpdateLike/', UpdateLike, name='UpdateLike'),
    path('MaxLike/', MaxPostLike, name='MaxLike'),
    path('LastDate/', LastDate, name='LastDate'),
    path('captcha', CaptchaView, name='CaptchaView'),
    path('SearchById/<str:id>/', SearchById, name='SearchById'),
    path('uploadimage/' , uploadImageViews , name='uploadImageViews'),
    path('uploaddata/' , uploadData , name='uploadData'),



    path('homeMokebPooyesh/', PostViewsMokebPooyesh, name='homeMokebPooyesh'),
    path('UpdateLikeMokebPooyesh/', UpdateLikeMokebPooyesh, name='UpdateLikeMokebPooyesh'),
    path('MaxLikeMokebPooyesh/', MaxPostLikeMokebPooyesh, name='MaxLikeMokebPooyesh'),
    path('LastDateMokebPooyesh/', LastDateMokebPooyesh, name='LastDateMokebPooyesh'),
    path('captchaMokebPooyesh', CaptchaViewMokebPooyesh, name='CaptchaViewMokebPooyesh'),
    path('SearchByIdMokebPooyesh/<str:id>/', SearchByIdMokebPooyesh, name='SearchByIdMokebPooyesh'),
  
    url(r'^media/(?P<path>.*)$', serve,
        {'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve,
        {'document_root': settings.STATIC_ROOT}),
    # url(r'^static/(.*)', serve,
    #     {'document_root': settings.STATIC_ROOT}),


]


urlpatterns  +=  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
