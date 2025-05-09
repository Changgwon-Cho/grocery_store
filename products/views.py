from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm
from django.contrib.auth.decorators import login_required, user_passes_test

def is_staff(user):
    return user.is_authenticated and user.role == 'staff'

@login_required
@user_passes_test(is_staff)
def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products}) 

@login_required
@user_passes_test(is_staff)
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'products/product_create.html', {'form': form})

@login_required
@user_passes_test(is_staff)
def product_update(request, pk):
    product = Product.objects.get(pk=pk)
    if request.method == 'POST': 
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'products/product_update.html', {'form': form, 'product': product})