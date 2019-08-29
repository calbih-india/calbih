from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about-us.html')

def whatwedo(request):
    return render(request, 'what-we-do.html')

def career(request):
    return render(request, 'career.html')

def contact(request):
    return render(request, 'contact.html')

def research_students(request):
    return render(request, 'research-students.html')

def academic_research_institutions(request):
    return render(request, 'academic-research-institutions.html')
