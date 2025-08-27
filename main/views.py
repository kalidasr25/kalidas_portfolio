from django.shortcuts import render

def home(request):
    return render(request, 'main/home.html')

def about(request):
    return render(request, 'main/about.html')

def skills(request):
    return render(request, 'main/skills.html')

def education(request):
    return render(request, 'main/education.html')

def projects(request):
    return render(request, 'main/projects.html')

def experience(request):
    return render(request, 'main/experience.html')

def contact(request):
    return render(request, 'main/contact.html')
