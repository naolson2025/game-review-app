from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

# Found login tutorial https://simpleisbetterthancomplex.com/tutorial/2017/02/18/how-to-create-user-sign-up-view.html
urlpatterns = [
    path('', views.home, name='home'),
    path('make_review', views.make_review, name='make_review'),
    path('all_reviews', views.all_reviews, name='all_reviews'),
    path(r'^signup/$', views.signup, name='signup'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='webApp/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(template_name='webApp/home.html'), name='logout'),
    path('accounts/profile/', views.my_reviews, name='my_reviews')
]
