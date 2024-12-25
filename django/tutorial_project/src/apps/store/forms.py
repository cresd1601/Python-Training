from django import forms
from .models import Category, Product, CartItem

# Consistent TextInput and Textarea widget settings
TEXTINPUT_WIDGET = forms.TextInput(attrs={'size': 50})  # Standard size for single-line text fields
TEXTAREA_WIDGET = forms.Textarea(attrs={'rows': 4, 'cols': 50})  # Standard size for multi-line text fields
NUMERIC_TEXTINPUT_WIDGET = forms.NumberInput(attrs={'style': 'width: 120px'})  # Standard size for numeric fields
SELECT_WIDGET = forms.Select(attrs={'style': 'width: 120px'})  # Consistent size for dropdown fields


# Custom form for Category model
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']
        widgets = {
            'name': TEXTINPUT_WIDGET,  # Consistent size for the name field
            'description': TEXTAREA_WIDGET,  # Consistent size for the description field
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 3:
            raise forms.ValidationError("Name must be at least 3 characters long.")
        if len(name) > 50:
            raise forms.ValidationError("Name must not exceed 50 characters.")
        if not self.instance.pk:  # Check uniqueness when adding a new category
            if Category.objects.filter(name=name).exists():
                raise forms.ValidationError("A category with this name already exists.")
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description')
        if len(description) < 10:
            raise forms.ValidationError("Description must be at least 10 characters long.")
        if len(description) > 200:
            raise forms.ValidationError("Description must not exceed 200 characters.")
        return description


# Custom form for Product model
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category', 'price', 'quantity_stock', 'description']
        widgets = {
            'name': TEXTINPUT_WIDGET,  # Consistent size for the name field
            'category': SELECT_WIDGET,  # Consistent size for the category dropdown
            'price': NUMERIC_TEXTINPUT_WIDGET,  # Consistent size for price
            'quantity_stock': NUMERIC_TEXTINPUT_WIDGET,  # Consistent size for quantity_stock
            'description': TEXTAREA_WIDGET,  # Consistent size for the description field
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 3:
            raise forms.ValidationError("Name must be at least 3 characters long.")
        if len(name) > 50:
            raise forms.ValidationError("Name must not exceed 50 characters.")
        if not self.instance.pk:  # Only check for uniqueness when adding a new product
            if Product.objects.filter(name=name).exists():
                raise forms.ValidationError("A product with this name already exists.")
        return name

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price <= 0:
            raise forms.ValidationError("Price must be positive.")
        if price > 10000:
            raise forms.ValidationError("Price must not exceed $10,000.")
        return price

    def clean_quantity_stock(self):
        quantity_stock = self.cleaned_data.get('quantity_stock')
        if quantity_stock < 0:
            raise forms.ValidationError("Quantity in stock cannot be negative.")
        return quantity_stock


# Custom form for CartItem model
class CartItemForm(forms.ModelForm):
    class Meta:
        model = CartItem
        fields = ['product', 'quantity']
        widgets = {
            'product': SELECT_WIDGET,  # Consistent size for the product dropdown
            'quantity': NUMERIC_TEXTINPUT_WIDGET,  # Consistent size for quantity field
        }

    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')
        product = self.cleaned_data.get('product')
        if quantity <= 0:
            raise forms.ValidationError("Quantity must be positive.")
        if product and quantity > product.quantity_stock:
            raise forms.ValidationError(f"Cannot add more than {product.quantity_stock} items of {product.name}.")
        return quantity

    def clean_product(self):
        product = self.cleaned_data.get('product')
        if not product:
            raise forms.ValidationError("A product must be selected.")
        return product
