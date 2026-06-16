from bird_app.models import Accessory, Bird, Cage


class Basket:
    MODEL_MAP = {
        'accessory': Accessory,
        'bird': Bird,
        'cage': Cage,
    }

    def __init__(self, request):
        self.session = request.session
        basket = self.session.get('basket')
        if not basket:
            basket = self.session['basket'] = {}
        self.basket = basket

    def _make_key(self, product_type, product_id):
        return f'{product_type}:{product_id}'

    def __iter__(self):
        basket_copy = self.basket.copy()

        ids_by_type = {ptype: [] for ptype in self.MODEL_MAP}
        for key in basket_copy.keys():
            product_type, product_id = key.split(':', 1)
            if product_type in ids_by_type:
                ids_by_type[product_type].append(int(product_id))

        objects_by_key = {}
        for product_type, ids in ids_by_type.items():
            if not ids:
                continue
            model = self.MODEL_MAP[product_type]
            for obj in model.objects.filter(pk__in=ids):
                objects_by_key[self._make_key(product_type, obj.pk)] = obj

        for key, item in basket_copy.items():
            product_type, _ = key.split(':', 1)
            product = objects_by_key.get(key)
            if not product:
                continue

            item['product'] = product
            item['product_type'] = product_type
            item['total_price'] = float(item['price']) * int(item['count'])
            yield item

    def __len__(self):
        return sum(item['count'] for item in self.basket.values())

    def save(self):
        self.session.modified = True

    def add(self, product, product_type, count=1, update_count=False):
        key = self._make_key(product_type, product.id)
        if key not in self.basket:
            self.basket[key] = {
                'count': 0,
                'price': float(product.price),
                'product_type': product_type,
            }
        if update_count:
            self.basket[key]['count'] = count
        else:
            self.basket[key]['count'] += count
        self.save()

    def remove(self, product_type, product_id):
        key = self._make_key(product_type, product_id)
        if key in self.basket:
            del self.basket[key]
            self.save()

    def get_total_price(self):
        return sum(float(item['price']) * int(item['count']) for item in self.basket.values())

    def clear(self):
        if 'basket' in self.session:
            del self.session['basket']
            self.session.modified = True