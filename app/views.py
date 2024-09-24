from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def founder(request):
    return render(request, 'founder.html')

def investor(request):
    return render(request, 'investor.html')

def experts(request):
    return render(request, 'experts.html')
