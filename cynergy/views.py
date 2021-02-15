from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request, 'cynergy/signup.html')

def about(request):
    return render(request, 'cynergy/about_us.html')    