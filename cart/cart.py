from decimal import Decimal
from django.conf import settings

from store.models import Cake


class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, cake):
        cake_id = str(cake.id)
        if cake_id not in self.cart:
            self.cart[cake_id] = {'quantity': 0, 'price': str(cake.price)}
            self.cart[cake_id]['quantity'] = 1
        else:    
            if self.cart[cake_id]['quantity'] < 10:
                self.cart[cake_id]['quantity'] += 1
        self.save()

    def update(self, cake, quantity):
        cake_id = str(cake.id)
        self.cart[cake_id]['quantity'] = quantity
        
        self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def remove(self, cake):
        cake_id = str(cake.id)
        if cake_id in self.cart:
            del self.cart[cake_id]
            self.save()

    def __iter__(self):
        cake_ids = self.cart.keys()
        cakes = Cake.objects.filter(id__in=cake_ids)
        for cake in cakes:
            self.cart[str(cake.id)]['cake'] = cake

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
