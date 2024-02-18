from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def create_customer(customer):
        return Customer.objects.create(customer)

    def get_customers():
        return Customer.objects.all()


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    item = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.item} - {self.customer}"

    def create_order(order):
        return Order.objects.create(order)

    def get_customer_orders(customer):
        return Order.objects.filter(customer=customer)
