from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm, ProductEditForm
# To display message
from django.contrib import messages
# Login required
from django.contrib.auth.decorators import login_required


# CRUD - Create, Read, Update, Delete

@login_required(login_url='accounts:login')
# Read
def product_list(request):
    products = Product.objects.all()
    return render(request, 'crud/product_list.html', {'products': products})
# End of read

# Create
def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crud:list_products')
    else:
        form = ProductForm()
    return render(request, 'crud/create_product.html', {'form': form})
# End of create

# Update
def update_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductEditForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "Product details updated successfully!")
            return redirect('crud:list_products')
    else:
        form = ProductEditForm(instance=product)
    context = {
        'form': form
    }
    return render(request, 'crud/update_product.html', context)
# End of update

# Delete
def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        # Success message
        messages.success(request, "Product deleted successfully!")
        return redirect('crud:list_products')
    return render(request, 'crud/delete_product.html', {'product': product})
# End of delete
