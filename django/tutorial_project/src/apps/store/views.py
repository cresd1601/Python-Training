# views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Category  # Import Category model


def index(request):
    products = Product.objects.all()  # Retrieve all products
    categories = Category.objects.all()  # Retrieve all categories

    if request.method == 'POST':
        # Check if the request is to add a product
        if 'add_product' in request.POST:
            name = request.POST.get('product_name')
            description = request.POST.get('description')
            price = request.POST.get('price')
            quantity_stock = request.POST.get('quantity_stock')
            category_id = request.POST.get('category')  # Get selected category

            # Create and save the new product
            Product.objects.create(
                name=name,
                description=description,
                price=price,
                quantity_stock=quantity_stock,
                category_id=category_id  # Set the category
            )
            return redirect('index')  # Redirect to the product list after adding

        # Check if the request is to delete a product
        elif 'delete_product' in request.POST:
            product_id = request.POST.get('product_id')
            product = get_object_or_404(Product, id=product_id)
            product.delete()  # Delete the product
            return redirect('index')  # Redirect to the product list after deletion

    return render(request, 'index.html', {'products': products, 'categories': categories})
