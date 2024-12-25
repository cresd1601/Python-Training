from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    description = models.CharField(max_length=200, blank=False, null=False)

    def __str__(self):
        return self.name


# Custom Manager for Products with quantity greater than zero
class ProductManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(quantity_stock__gt=0)


class ProductQuerySet(models.QuerySet):
    # Filter by category name
    def get_by_category_name(self, category_name):
        return self.filter(category__name=category_name)


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=False, null=False)
    description = models.CharField(max_length=200, blank=False, null=False)
    price = models.FloatField(default=0.0)
    quantity_stock = models.IntegerField(default=0)

    # Use custom QuerySet
    objects = ProductQuerySet.as_manager()

    # Custom manager
    custom_manager = ProductManager()  # Custom manager for available products

    def __str__(self):
        return self.name


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.product.name} (Quantity: {self.quantity})"
