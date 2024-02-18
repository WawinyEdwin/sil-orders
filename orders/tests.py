import json

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from orders.models import Customer


class CustomerTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="password")
        self.token = Token.objects.create(user=self.user)

    def test_customer_create(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)
        response = self.client.post(
            path="/api/customers/",
            data={"name": "John Doe", "code": "J9D", "phone": "+254759701314"},
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Customer.objects.count(), 1)
        self.assertEqual(Customer.objects.get().name, "John Doe")

    def test_customer_list(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)
        response = self.client.get(path="/api/customers/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class OrderTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="password")
        self.token = Token.objects.create(user=self.user)
        self.customer = Customer.objects.create(
            name="Jane Doe", code="JoD", phone="+254759701314"
        )

    def test_order_create(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)
        url = reverse("orders", kwargs={"customer_id": self.customer.pk})
        response = self.client.post(
            path=url,
            data=json.dumps(
                {"customer": self.customer.pk, "item": "Hisense", "amount": 1000}
            ),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_order_list(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)
        url = reverse("orders", kwargs={"customer_id": self.customer.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
