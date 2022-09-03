from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def ferrari(request):
    return render(request,"ferrari.html")