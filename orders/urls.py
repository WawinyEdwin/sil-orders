from django import views
from django.urls import path, re_path

from orders import views

urlpatterns = [
    path("customers/", views.customers, name="customers"),
    path("customers/<int:customer_id>/orders/", views.customer_orders, name="orders"),
    re_path(
        "register-by-access-token/" + r"social/(?P<backend>[^/]+)/$",
        views.register_by_access_token,
    ),
]
