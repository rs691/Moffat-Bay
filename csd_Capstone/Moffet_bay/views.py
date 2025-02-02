from django.shortcuts import render







def projects(request):
    return render(request, 'Moffet_bay/projects.html')



def index(request):
    return render(request, 'Moffet_bay/index.html')

def registration(request):
    return render(request, 'Moffet_bay/registration.html')

def login(request):
    return render(request, 'Moffet_bay/login.html')

