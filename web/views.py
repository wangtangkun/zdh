from django.shortcuts import render,HttpResponse,redirect
from django.http import JsonResponse

# Create your views here.

def index(request):
    return render(request,"index.html")