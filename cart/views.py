from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

from store.models import Cake, Category
from .cart import Cart

def cart_add(request, cakeid):
	cart = Cart(request)  
	cake = get_object_or_404(Cake, id=cakeid) 
	cart.add(cake=cake)
	return redirect('store:index')

def cart_update(request, cakeid, quantity):
	cart = Cart(request) 
	cake = get_object_or_404(Cake, id=cakeid) 
	cart.update(cake=cake, quantity=quantity)
	price = (cake.price * quantity)

	return render(request, 'cart/price.html', {"price":price})

def cart_remove(request, cakeid):
    cart = Cart(request)
    cake = get_object_or_404(Cake, id=cakeid)
    cart.remove(cake)
    return redirect('cart:cart_details')

def total_cart(request):
	return render(request, 'cart/totalcart.html')

def cart_summary(request):
	return render(request, 'cart/summary.html')

def cart_details(request):
	cart = Cart(request)
	context = {
		"cart": cart,
	}
	return render(request, 'cart/cart.html', context)
