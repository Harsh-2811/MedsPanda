from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"home.html")

def policy(request):
    return render(request,"page-privacy.html")

def terms(request):
    return render(request,"page-terms.html")
    