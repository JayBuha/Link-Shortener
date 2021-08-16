from django.shortcuts import render
import pyshorteners

# Create your views here.

def home(request):
    return render(request, 'home.html')

def short(request): 

    link = request.POST.get('url')

    Shortener = pyshorteners.Shortener()

    x = Shortener.tinyurl.short(link)

    return render(request,'home.html',{'URL':x})