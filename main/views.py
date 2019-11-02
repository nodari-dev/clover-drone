from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import News, Updates
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, authenticate, login
from django.middleware.csrf import CsrfViewMiddleware
def homepage(request):
    return render(request=request, template_name="main/index.html")

def newspage(request):
    return render(request=request, template_name="main/news.html", context={'clover': News.objects.all})
def downloadpage(request):
	return render(request=request, template_name="main/download.html")
def updatespage(request):
	return render(request=request, template_name="main/updates.html", context={'clover_updates': Updates.objects.all})
# Create your views here.
