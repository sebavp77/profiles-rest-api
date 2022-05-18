###################################################################
########## This is a complete new file that I created ############
########## To include new URLs resources #########################

from django.urls import path
from profiles_api import views

urlpatterns = [
#I create a new url named 'hello-view' which is mapped to views.HelloApiView.as_view
    path('hello-view/',views.HelloApiView.as_view())
]
