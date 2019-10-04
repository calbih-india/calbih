from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about-us.html')

def technology(request):
    return render(request, 'technology.html')

def consulting(request):
    return render(request, 'consulting.html')

def contact(request):
    return render(request, 'contact-us.html')

def trade(request):
    return render(request, 'trade.html')

def blogs_list(request):
    return render(request, 'blogs-list.html')

def blog_details(request):
    return render(request, 'blog-details.html')
