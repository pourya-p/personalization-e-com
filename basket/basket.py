from store.models import Product


class Basket:
    def __init__(self, request):
        self.session = request.session

        if 'basket' in request.session:
            basket = self.session.get('basket')
        else:
            basket = self.session['basket'] = {}

        self.basket = basket

    def add(self, product, qty):
        product_id = str(product.id)

        if product_id in self.basket:
            self.basket[product_id]["qty"] += qty

        else:
            self.basket[product_id] = {'qty': qty}

        self.save()

    def total_price(self):
        product_key = self.basket.keys()
        total_price = 0
        for key in product_key:
            product = Product.objects.get(id=key)
            qty = self.basket[key]['qty']
            total_price += product.price * qty

        return total_price

    def __len__(self):
        return len(self.basket)

    def __iter__(self):
        product_key = self.basket.keys()

        for key in product_key:
            product = Product.objects.get(id=key)
            qty = self.basket[key]['qty']
            total_price = product.price * qty
            yield {'product': product, 'qty': qty, 'total_price': total_price}

    def save(self):
        self.session.modified = True
