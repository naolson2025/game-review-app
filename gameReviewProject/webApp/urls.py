from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

# Found login tutorial https://simpleisbetterthancomplex.com/tutorial/2017/02/18/how-to-create-user-sign-up-view.html
urlpatterns = [
    path('', views.all_reviews, name='all_reviews'),
    path('make_review', views.make_review, name='make_review'),
    path(r'^signup/$', views.signup, name='signup'),
    path('search_video', views.search_video, name='search_video'),
    path('blank_new_review', views.blank_new_review, name='blank_new_review'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='webApp/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(template_name='webApp/all_reviews.html'), name='logout'),
    path('accounts/profile/', views.my_reviews, name='my_reviews')
]
