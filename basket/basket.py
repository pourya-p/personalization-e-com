from store.models import Product, ProductInventory


class Basket:
    def __init__(self, request):
        self.session = request.session

        if 'skey' in request.session:
            basket = self.session.get('skey')
        else:
            basket = self.session['skey'] = {}

        self.basket = basket

    def add(self, product, qty):
        product = product

        if product.sku in self.basket:
            self.basket[product.sku]["qty"] += qty

        else:
            self.basket[product.sku] = {'qty': qty}

        self.save()

    def basket_total_price(self):
        product_key = self.basket.keys()
        total_price = 0
        for key in product_key:
            product_inv = ProductInventory.objects.get(sku=str(key))
            qty = self.basket[key]['qty']
            total_price += product_inv.price * qty

        return total_price

    def __len__(self):
        return len(self.basket)

    def __iter__(self):
        product_key = self.basket.keys()

        for key in product_key:
            product_inv = ProductInventory.objects.get(sku=key)
            qty = self.basket[key]['qty']
            total_price = product_inv.price * qty
            for_yield = {'product_inv': product_inv,
                         'qty': qty,
                         'total_price': total_price,
                         }
            yield for_yield

    def save(self):
        self.session.modified = True
