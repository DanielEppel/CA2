from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Product
from .cart import Cart
from .forms import CartAddProductForm
from vouchers.forms import VoucherApplyForm
from django.conf import settings
import stripe
# Create your views here.
@require_POST
def add_cart(request, product_id):
	cart = Cart(request)
	product = Product.objects.get(Product, id=product_id)
	form = CartAddProductForm(request_POST)
	if forms.is_valid():
		cd = form.cleaned_data
		cart.add(product=product, 
				quantity=cd['Quanatity'],
				update_quantity=cd['update'])
	return redirect('cart:cart_detail')
	

	
def cart_detail(request):
	cart = Cart(request)
	for item in cart:
		item['update_quantity_form'] = CartAddProductForm(
								initial={'quantity' : item['quantity'],
								'update': True})

	voucher_apply_form = VoucherApplyForm()
	
	stripe.api_key = settings.STRIPE_SECRET_KEY
	stripe_total = int(total*100)
	description = 'online Shop - New Order'
	data_key = settings.STRIPE_PUBLISHABLE_KEY
	return render(request, 'cart/cart_detail.html',{'cart':cart},
					'voucher_apply_form': voucher_apply_form,
					 dict(data_key = data_key, stripe_total = stripe_total, description = description))
					
def cart_remove(request, product_id):
	cart = Cart(request)
	product = get_object_or_404(Product, id=product_id)
	cart.remove(product)
	return redirect('cart:cart_detail')
	

