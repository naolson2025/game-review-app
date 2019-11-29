from django.shortcuts import render, HttpResponse


# When the '' url is entered into the browser this method is called.
# This method will render the home.html template
def home(request):
    return render(request, 'webApp/home.html')