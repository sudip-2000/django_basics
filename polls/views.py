from django.shortcuts import render
from  django.http import HttpResponse


def home(request):
    return render(request, 'polls/home.html')

def about(request):
    return render(request, 'polls/about.html')

def contact(request):
    return HttpResponse("<h2>Feel free to contact</h2>")



