from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from .models import Cart
# from .model import Member

def index(request):
    return render(request,
                  'secondapp/index.html',
                  {})

def getCartList(request):
    cart_list = Cart.objects.all()
    return render(request,
                  'secondapp/cart/cart_list.html',
                  {"cart_list":cart_list})


