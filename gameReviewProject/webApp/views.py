from django.shortcuts import render, HttpResponse



def home(request):
    render(request, 'home.html')