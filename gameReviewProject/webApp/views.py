from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import NewReviewForm
from .models import Review



# When the '' url is entered into the browser this method is called.
# This method will render the home.html template
def home(request):
    return render(request, 'webApp/home.html')



@login_required
def make_review(request):   
    # If the request is a POST than take the information given from the user in the form
    if request.method == 'POST':
        # Creates a form instance and populate the data with what the user provided
        new_review_form = NewReviewForm(request.POST, request.FILES)
        # don't save the form yet until the user is verified
        #review = form.save(commit=False)
        # Assign the user
        #review.user = request.user
        # Save the form
        if new_review_form.is_valid():
            review = new_review_form.save(commit=False)
            review.user = request.user
            review.save()
            # after the form is saved reload the make review page
            return redirect('my_reviews')
        else:
            return render(request, 'webApp/make_review.html', {'new_review_form': new_review_form})

    # If the request is not a POST request than render a blank form
    new_review_form = NewReviewForm()
    # send the new review form as a variable that can be used in the makereview.html template
    return render(request, 'webApp/make_review.html', {'new_review_form': new_review_form})



def all_reviews(request):
    # Gets all Review objects from the database
    reviews = Review.objects.all().order_by('game_name')
    # Sends all review objects to be rendered on all_reviews.html
    return render(request, 'webApp/all_reviews.html', {'reviews': reviews})



@login_required
def my_reviews(request):
    my_reviews = Review.objects.filter(user=request.user)
    return render(request, 'webApp/my_reviews.html', {'my_reviews': my_reviews})



# Found signup tutorial https://simpleisbetterthancomplex.com/tutorial/2017/02/18/how-to-create-user-sign-up-view.html
def signup(request):
    if request.method == 'POST':
        user_creation_form = UserCreationForm(request.POST)
        if user_creation_form.is_valid():
            user_creation_form.save()
            username = user_creation_form.cleaned_data.get('username')
            raw_password = user_creation_form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        user_creation_form = UserCreationForm()
    return render(request, 'webApp/signup.html', {'user_creation_form': user_creation_form})