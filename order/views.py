from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm 
from cart.cart import Cart
from django.contrib.auth.decorators import login_required
import stripe 
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import get_objects_or_404
from models import Order

@login_required()
def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.fillter(cart=cart)
        if form.is_valid():
            oder = form.save(commit=False)
            if cart.voucher:
                order.voucher = cart.voucher
                order.discount = cart.voucher.discount
            order.save() 
            for item in cart:
                OrderItem.objects.create(order=order,
                                        product=item['product'],
                                        price=item['price'],
                                        quantity=item['quantity'])
            cart.clear()
            return render(request,
                            'order/created.html',
                            {'order': order})
        for item in cart_items:
            total += (item.quantity * item.product.price)
        print('total', total)
        charge = stripe.Change.create(
            amount=str(int(total*100)),
            currency='EUR',
            description= 'Credit Card Charge',
            source= request.POST['stripeToken']) 
    if request.user.is_authenticated:
        email = str(request.user.email)
        order_details = Order.objects.create(emailAddress = email)
        order_details.save()
    else:
        form = OrderCreateForm()
    return render(request,
                    'order/create.htlm',
                    {'cart':cart, 'form':form})

    
@login_required()
def order_history(request):
    if request.user.is_authenticated:
        email = str(request.user.email)
        order_details = order.objects.fillter(emailAddress = email)
    return render(request, 'order_list.html', {'order_details':order_details})

@staff_member_required
def admin_order_detail(request, order_id):
    Order = get_objects_or_404(order. id=order_id)
    return render(request,
                   'admin/order/order/detail.html',
                   {'order':order})