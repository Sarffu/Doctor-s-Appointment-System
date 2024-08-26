from django.shortcuts import render


# Create your views here.
def About(request):
    return render(request, "about.html")

def Navigation(request):
    return render(request, 'navigation.html')