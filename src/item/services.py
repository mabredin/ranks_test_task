from typing import NewType, Protocol

import stripe
from stripe.api_resources.checkout import Session

from config import settings

StripeSessionId = NewType("StripeSessionId", str)


class StripeLineItemsConvertable(Protocol):
    def to_stripe_line_items(self) -> list[Session.CreateParamsLineItem]:
        ...


def create_stripe_session(obj: StripeLineItemsConvertable) -> StripeSessionId:
    session = stripe.checkout.Session.create(
        line_items=obj.to_stripe_line_items(),
        mode="payment",
        success_url=f"{settings.SOURCE_BASE_URL}/success/",
        cancel_url=f"{settings.SOURCE_BASE_URL}/cancel/",
    )
    return StripeSessionId(session["id"])
