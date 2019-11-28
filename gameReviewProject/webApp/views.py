from django.shortcuts import render, HttpResponse



def home(request):
    render(request, 'webApp/home.html')