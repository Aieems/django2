from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

from bird_app.models import Accessory, Bird, Cage, Order, Pos_order
from .basket import Basket
from .forms import BasketAddProductForm, OrderForm


PRODUCT_MODEL_MAP = {
    'accessory': Accessory,
    'bird': Bird,
    'cage': Cage,
}


def basket_detail(request):
    basket = Basket(request)
    return render(request, 'basket/detail.html', {'basket': basket})


def basket_remove(request, product_type, product_id):
    basket = Basket(request)
    basket.remove(product_type=product_type, product_id=product_id)
    return redirect('basket_detail')


def basket_clear(request):
    basket = Basket(request)
    basket.clear()
    return redirect('basket_detail')


@require_POST
def basket_add(request, product_type, product_id):
    model = PRODUCT_MODEL_MAP.get(product_type)
    if model is None:
        return redirect('basket_detail')

    basket = Basket(request)
    product = get_object_or_404(model, pk=product_id)

    form = BasketAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        basket.add(
            product=product,
            product_type=product_type,
            count=cd['count'],
            update_count=cd['reload'],
        )
    return redirect('basket_detail')


@login_required
def basket_buy(request):
    basket = Basket(request)
    if len(basket) <= 0:
        return redirect('products')

    form = OrderForm(request.POST)
    if form.is_valid():
        order = Order.objects.create(
            user=request.user,
            buyer_firstname=form.cleaned_data['buyer_firstname'],
            buyer_name=form.cleaned_data['buyer_name'],
            buyer_surname=form.cleaned_data['buyer_surname'],
            comment=form.cleaned_data['comment'],
            delivery_address=form.cleaned_data['delivery_address'],
            delivery_type=form.cleaned_data['delivery_type'],
            price=basket.get_total_price(),
        )

        for item in basket:
            kwargs = {
                'order': order,
                'count': item['count'],
            }
            if item['product_type'] == 'accessory':
                kwargs['accessory'] = item['product']
            elif item['product_type'] == 'bird':
                kwargs['bird'] = item['product']
            elif item['product_type'] == 'cage':
                kwargs['cage'] = item['product']

            Pos_order.objects.create(**kwargs)

        basket.clear()
        return redirect('basket_detail')

    return redirect('order_open')


@login_required
def open_order(request):
    context = {
        'form_order': OrderForm(),
    }
    return render(request, 'order/order_form.html', context)