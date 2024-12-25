import csv
from django.http import HttpResponse
from django.contrib import admin
from .models import Category, Product, CartItem
from .forms import CategoryForm, ProductForm, CartItemForm  # Import custom forms

# Customize the admin site appearance
admin.site.site_header = "My E-Commerce Admin"
admin.site.site_title = "E-Commerce Admin Portal"
admin.site.index_title = "Welcome to the E-Commerce Admin"


# Custom action to export categories to CSV
@admin.action(description="Export selected categories to CSV")
def export_categories_to_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="categories.csv"'
    writer = csv.writer(response)
    writer.writerow(['Name', 'Description'])  # Header row

    for category in queryset:
        writer.writerow([category.name, category.description])  # Data rows

    return response


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    form = CategoryForm
    list_display = ["name", "description"]
    fieldsets = (
        (None, {
            'fields': ('name',)
        }),
        ('Description', {
            'fields': ('description',)
        }),
    )
    search_fields = ["name"]
    list_filter = ["name"]
    actions = [export_categories_to_csv]  # Add the CSV export action


# Custom action to export products to CSV
@admin.action(description="Export selected products to CSV")
def export_products_to_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="products.csv"'

    writer = csv.writer(response)
    writer.writerow(['Name', 'Category', 'Price', 'Quantity Stock', 'Description'])  # Header row

    for product in queryset:
        writer.writerow([product.name, product.category.name, product.price, product.quantity_stock, product.description])  # Data rows

    return response


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    form = ProductForm
    list_display = ["name", "category", "price", "quantity_stock", "description"]
    fieldsets = (
        (None, {
            'fields': ('name', 'category')
        }),
        ('Description', {
            'fields': ('description',)
        }),
        ('Pricing and Stock', {
            'fields': ('price', 'quantity_stock'),
        }),
    )
    search_fields = ["name", "category__name"]
    list_filter = ["category", "price"]
    ordering = ["-price"]
    actions = [export_products_to_csv]  # Add the CSV export action


# Custom action to export cart items to CSV
@admin.action(description="Export selected cart items to CSV")
def export_cart_items_to_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="cart_items.csv"'

    writer = csv.writer(response)
    writer.writerow(['Product', 'Quantity'])  # Header row

    for cart_item in queryset:
        writer.writerow([cart_item.product.name, cart_item.quantity])  # Data rows

    return response


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    form = CartItemForm
    list_display = ["product", "quantity"]
    fieldsets = (
        (None, {
            'fields': ('product',)
        }),
        ('Quantity', {
            'fields': ('quantity',),
        }),
    )
    search_fields = ["product__name"]
    list_filter = ["quantity"]
    actions = [export_cart_items_to_csv]  # Add the CSV export action
