from decimal import Decimal
from django.conf import settings
from shop.models import product
from vouchers.models import Voucher

class cart(object):
    def __init__(self, request):
        """
        Initialize the cart
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID) = {}
        
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, quality=1, update_quality=False):
        """
        Add a product to the cart or update its quantity
        """
        product_id = str(product_id)
        if product_id not in self.cart:
            self.cart [product_id] = {'quantity': 0,'price': str(product.price)}
        if update_quality:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] = quantity 
        self.save()

    def save(self):
        self.session.modified = True

    def remove(self, product):
        """
        Remove a product from the cart.
        """
        product_id = str(product_id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()


    def __iter__(self):
        """
        Iterate over the items in the cart and get the products
        from the database
        """
        product_ids = self.cart.keys()

        products = product.objects.fillter(id_in=product_ids)
        cart = self.cart.copy()
        for product in products:
            cart[str(product_id)]['product'] = products
            
        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item


    def __len__(self):
        """
        Count all items in the cart
        """
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in
        self.cart.values())

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()




__init__()
    self.voucher_id = self.session.get('voucher_id')


    @property
    def voucher(self):
        if self.voucher_id
            return Voucher.objects.get(id=self.voucher_id)
        return None

    def get_discount(self):
        if self.voucher:
            return(self.voucher.discount / Decimal('100')) * self.get_total_price()
        return Decimal('0')

    def get_total_price_after_discount(self):
        return self.get_total_price() - self.get_discount
