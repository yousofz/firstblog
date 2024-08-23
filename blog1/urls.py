from django.urls import path
#from . import views
from .views import HomeView , PostView
urlpatterns = [
#    path('', views.home,name="home"),
    path('',HomeView.as_view(),name="Home"),
    path('post/<int:pk>',PostView.as_view(),name="postview"),
    
]
