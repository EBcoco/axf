from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from app.models import Wheel


def home(request):
    wheels=Wheel.objects.all()
    return render(request, 'home/home.html',context={"wheels":wheels})


def market(request):
    return render(request, 'market/market.html')


def cart(request):
    return render(request, 'cart/cart.html')


def mine(request):
    return render(request, 'mine/mine.html')