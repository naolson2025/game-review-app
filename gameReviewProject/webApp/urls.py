from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('make_review', views.make_review, name='make_review')
]
