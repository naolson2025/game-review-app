from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import NewReviewForm, NewSearchForm
from .models import Review, Search
from .youtube_api import main


# When the '' url is entered into the browser this method is called.
# This method will render the home.html template
# This method is not used in the running app, it was a placeholder during development
def home(request):
    return render(request, 'webApp/home.html')



# Render make_review.html with two blank forms
@login_required
def blank_new_review(request):
    new_review_form = NewReviewForm()
    new_search_form = NewSearchForm()
    return render(request, 'webApp/make_review.html', {'new_review_form': new_review_form, 'new_search_form': new_search_form})



@login_required
def make_review(request):   
    # If the request is a POST than take the information given from the user in the form
    # The request should always be a POST because there is no button associated with this link that is not a POST
    if request.method == 'POST':
        # Creates a form instance and populate the data with what the user provided
        new_review_form = NewReviewForm(request.POST, request.FILES)
        # Blank video search form for rendering if the form validation fails
        new_search_form = NewSearchForm()
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
            return render(request, 'webApp/make_review.html', {'new_review_form': new_review_form, 'new_search_form': new_search_form})

    #This code should never be reached, leaving for reference
    #video_ids = main()
    # If the request is not a POST request than render a blank form
    #new_review_form = NewReviewForm()
    # send the new review form as a variable that can be used in the makereview.html template
    #return render(request, 'webApp/make_review.html', {'new_review_form': new_review_form, 'video_ids': video_ids})



@login_required
def search_video(request):
    # If the method is a POST request than take the information from the user to search for YouTub videos
    # This will always be POST as their are no buttons leading to this method without POST
    if request.method == 'POST':
        # Create a form instance for the new_review_form in order to save the user's data so they don't re-enter it
        new_review_form = NewReviewForm()
        # Get the user's entry into the YouTube video search form
        new_search_form = NewSearchForm(request.POST)
        print(new_search_form)
        if new_search_form.is_valid():
            search = new_search_form.save(commit=False)
            search.user = request.user
            search.save()
            print(Search.objects.all())
            video_ids = main()
            return render(request, 'webApp/make_review.html', {'new_review_form': new_review_form, 'new_search_form': new_search_form, 'video_ids': video_ids})
        else:
            return render(request, 'webApp/make_review.html', {'new_review_form': new_review_form, 'new_search_form': new_search_form})



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