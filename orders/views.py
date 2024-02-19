from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from social_django.utils import psa

from orders.models import Customer, Order
from orders.serializers import CustomerSerializer, OrderSerializer
from orders.services.sms import SmsService


@api_view(["GET"])
def home(request):
    return Response(
        {
            "message": "Welcome to the Orders API",
            "detail": "Visit the postman documentation https://documenter.getpostman.com/view/17474568/2sA2r823z9",
        },
        status=status.HTTP_200_OK,
    )


@api_view(["POST"])
@permission_classes([AllowAny])
@psa()
def register_by_access_token(request, backend):
    token = request.data.get("access_token")
    user = request.backend.do_auth(token)
    if user:
        token, _ = Token.objects.get_or_create(user=user)
        return Response(
            {"token": token.key},
            status=status.HTTP_200_OK,
        )
    return Response(
        {"errors": {"token": "Invalid token"}},
        status=status.HTTP_400_BAD_REQUEST,
    )


@api_view(["POST", "GET"])
@permission_classes([IsAuthenticated])
def customer_orders(request, customer_id):
    sms_service = SmsService()

    if request.method == "GET":
        orders = Order.get_customer_orders(customer_id)
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    if request.method == "POST":
        order = request.data
        order["customer"] = customer_id
        serializer = OrderSerializer(data=order)
        if serializer.is_valid():
            order = serializer.save()
            if order:
                sms_service.send(
                    order.customer.phone, f"New order created for {order.item}"
                )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def customers(request):
    if request.method == "GET":
        customers = Customer.get_customers()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == "POST":
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
