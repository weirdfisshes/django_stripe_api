import stripe
from django.conf import settings
from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import TemplateView

from .models import Item

CENTS_IN_DOLLAR = 100


class HomePageView(TemplateView):
    template_name = 'index.html'


def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    context = {
        'item': item,
    }
    return render(request, 'form.html', context)


@csrf_exempt
def stripe_config(request):
    if request.method == 'GET':
        stripe_config = {'publicKey': settings.STRIPE_PUBLISHABLE_KEY}
        return JsonResponse(stripe_config, safe=False)


def create_checkout_session(self, pk):
    stripe.verify_ssl_certs = settings.VERIFY_SSL_CERTS
    stripe.api_key = settings.STRIPE_SECRET_KEY
    item = get_object_or_404(Item, pk=pk)
    product = stripe.Product.search(
        query=f"active:'true' AND name:'{item.name}'",
    )
    data = product['data']
    if data:
        product_id = data[0]['id']
        product = stripe.Product.retrieve(product_id)
    else:
        product = stripe.Product.create(
            name=item.name,
            description=item.description,
        )
    price = stripe.Price.create(
        product=product.id,
        unit_amount=int(item.price * CENTS_IN_DOLLAR),
        currency='usd',
    )
    checkout_session = stripe.checkout.Session.create(
        line_items=[
            {
                'price': price.stripe_id,
                'quantity': 1
            }
        ],
        mode='payment',
        success_url='http://127.0.0.1:8000/success/',
        cancel_url='http://127.0.0.1:8000/cancelled/',
    )
    return JsonResponse({'sessionId': checkout_session['id']})


class SuccessView(TemplateView):
    template_name = 'success.html'


class CancelledView(TemplateView):
    template_name = 'cancelled.html'
