from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    date_registry = models.DateField()

    def __str__(self):
        return (f'Username: {self.name}, '
                f'email: {self.email}, '
                f'phone: {self.phone}, '
                f'address: {self.address}, '
                f'date_registry: {self.date_registry}')


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
    how_many = models.IntegerField()
    date_create = models.DateField()

    def __str__(self):
        return (f'name: {self.name}, '
                f'price: {self.price}, '
                f'description: {self.description}, '
                f'how_many: {self.how_many}, '
                f'date_create: {self.date_create}')


class Orders(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    date_ordered = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
