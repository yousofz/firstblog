from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import post

#def home(request):
#    return render(request,'home.html',{})
class HomeView (ListView):
    model = post
    template_name='home.html'
class PostView (DetailView):
    model=post
    template_name='postview.html'
