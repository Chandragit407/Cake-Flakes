from django.shortcuts import render
from django.http import HttpResponse
from . models import Product
from .models import Testimonials
# Create your views here.

def index(request):
    products = Product.objects.all()
    return render(request,"bakes/index.html",{'products':products})

def contact(request):
    return render(request,"bakes/contact.html")

def testimonials(request):
    testi = Testimonials.objects.all()
    return render(request,"bakes/testimonials.html",{'testi':testi})

def portfolio(request):
    return render(request,"bakes/portfolio.html")

def faq(request):
    return render(request,"bakes/faq.html")

def register(request):
    return render(request,"bakes/register.html")

def login(request):
    return render(request,"bakes/login.html")

def portfoliodetails(request):
    return render(request,"bakes/portfoliodetails.html")