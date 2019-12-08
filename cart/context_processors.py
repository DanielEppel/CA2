from .models import Cart, CartItem
from .views import _cart_id
from .cart import Cart

def cart(request):
	return{'cart': Cart(request)}

