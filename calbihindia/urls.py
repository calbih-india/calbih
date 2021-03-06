"""calbihindia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from django.urls import path

from django.conf.urls import url
from django.contrib import admin

from mysite import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('about-us/', views.about, name='about-us'),
    path('technology/', views.technology, name='technology'),
    path('consulting/', views.consulting, name='consulting'),
    path('contact-us/', views.contact, name='contact-us'),
    path('trade/', views.trade, name='trade'),
    path('blogs-list/', views.blogs_list, name='blogs-list'),
    path('blog-details/', views.blog_details, name='blog-details'),
    path('vichar-vidyapeeth/', views.vichar_vidyapeeth, name='vichar-vidyapeeth'),
    
]
