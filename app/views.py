from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from app.models import Wheel, Nav, Mustbuy, Shop, MainShow, Foodtypes, Goods


def home(request):
    wheels=Wheel.objects.all()

    navs=Nav.objects.all()

    mustbuys=Mustbuy.objects.all()

    shops =Shop.objects.all()
    shophead=shops[0]
    shoptabs=shops[1:3]
    shopclass=shops[3:7]
    shopcommend=shops[7:11]
    mainShows=MainShow.objects.all()

    return render(request, 'home/home.html',
                  context={"wheels":wheels,
                           "navs":navs,
                           "mustbuys":mustbuys,
                           "shophead":shophead,
                           "shoptabs":shoptabs,
                           "shopclass":shopclass,
                           "shopcommend":shopcommend,
                           "mainShows":mainShows
                           })

def market(request,categoryid):
    foodtypes=Foodtypes.objects.all()
    #没有时，默认为0
    typeIndex=int(request.COOKIES.get('typeIndex',0))
    categoryid =foodtypes[typeIndex].typeid

    # goodslist=Goods.objects.all()[0:10]
    goodslist = Goods.objects.filter(categoryid=categoryid)
    data={"foodtypes":foodtypes,
          "goodslist":goodslist,
          }
    return render(request, 'market/market.html' ,context=data)


def cart(request):
    return render(request, 'cart/cart.html')


def mine(request):
    return render(request, 'mine/mine.html')


def marketbase(request):
    return redirect('axf:market', 104749)