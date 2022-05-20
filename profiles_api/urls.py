###################################################################
########## This is a complete new file that I created ############
########## To include new URLs resources #########################

from django.urls import path
from profiles_api import views

########To create the router for our VIEWSet ###############
from django.urls import include #including list of URLs
from rest_framework.routers import DefaultRouter #importing routers


router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset') #the url we want to created
#the sencond argument is the viewset we want to register to that URL, the third
#argument is name for our viewset (retrieven the URLS in our router)
########## Registering the user ViewSet ###################################
router.register('profile',views.UserProfileViewSet)

urlpatterns = [
#I create a new url named 'hello-view' which is mapped to views.HelloApiView.as_view
    path('hello-view/',views.HelloApiView.as_view()),
    ######to include login API view
    path('login/',views.UserLoginApiView.as_view()),#this Enables
    #the django end point (to be seen on the browser)
    path('',include(router.urls))#creating the path to the VIEWsets
]
