from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.base import TemplateView
from .models import Item
import stripe
from .settings import STRIPE_SECRET_KEY


class ItemView(View):

    def get(self, request, id):

        item_object = Item.objects.filter(id=id).first()
        context = {'item_object': item_object}

        return render(request, "shopping_app/item.html", context=context)


class BuyView(View):

    def get(self, request, id):
        stripe.api_key = STRIPE_SECRET_KEY
        item = Item.objects.filter(id=id).first()
        session = stripe.checkout.Session.create(
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': item.name,
                    },
                    'unit_amount': item.price * 100,
                },
                'quantity': 1,
            }, ],
            mode='payment',
            success_url='http://localhost:8000/success',
            cancel_url='http://localhost:8000/cancel',
        )

        return redirect(session.url, code=303)


class SuccessView(TemplateView):
    template_name = 'shopping_app/success.html'


class CancelView(TemplateView):
    template_name = 'shopping_app/cancel.html'
