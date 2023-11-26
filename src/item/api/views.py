from rest_framework.generics import get_object_or_404
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import Item, Order
from ..services import create_stripe_session


class CreateCheckoutSessionForItemView(APIView):
    def get(self, request: Request, pk: int) -> Response:
        item = get_object_or_404(Item, pk=pk)
        return Response({"id": create_stripe_session(item)})


class CreateCheckoutSessionForOrderView(APIView):
    def get(self, request: Request, pk: int) -> Response:
        order = get_object_or_404(Order, pk=pk)
        return Response({"id": create_stripe_session(order)})
