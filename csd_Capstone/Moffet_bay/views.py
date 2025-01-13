from django.shortcuts import render




def contact(request):
    return render(request, 'Moffet_bay/contact.html')


def projects(request):
    return render(request, 'Moffet_bay/projects.html')



def index(request):
    return render(request, 'Moffet_bay/index.html')

