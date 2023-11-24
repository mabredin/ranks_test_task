from typing import NewType

import stripe

from config import settings
from .models import Item


StripeSessionId = NewType('StripeSessionId', str)


def create_stripe_session(item: Item) -> StripeSessionId:
    session = stripe.checkout.Session.create(
        line_items=[
            {
                'price_data': {
                    'currency': 'rub',
                    'product_data': {
                        'name': item.name,
                        'description': item.description,
                    },
                    'unit_amount_decimal': item.price * 100
                },
                'quantity': 1,
            }
        ],
        mode='payment',
        success_url=f'{settings.SOURCE_BASE_URL}/success/',
        cancel_url=f'{settings.SOURCE_BASE_URL}/cancel/'
    )
    return StripeSessionId(session['id'])
