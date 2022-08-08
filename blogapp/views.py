from poplib import POP3_SSL_PORT
from django.shortcuts import render,redirect,HttpResponse
from django.views import View
from.models import Post

# Create your views here.
def home(request):
    context={'posts':Post.objects.all()}
    return render(request,'home.html',context)

