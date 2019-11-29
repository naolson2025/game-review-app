from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required


# When the '' url is entered into the browser this method is called.
# This method will render the home.html template
@login_required
def home(request):
    return render(request, 'webApp/home.html')



@login_required
def make_review(request):
    return render(request, 'webApp/makereview.html')