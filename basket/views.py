from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import BasketAddForm
from .models import Basket

def is_staff(user):
    return user.is_authenticated and user.role == 'staff'

@login_required 
def add_to_basket(request):
    if request.user.role != 'customer':
        return redirect('home')  

    if request.method == 'POST':
        form = BasketAddForm(request.POST)
        if form.is_valid():
            basket = form.save(commit=False) 
            basket.customer = request.user 
            basket.status = 'pending'
            basket.save()
            return redirect('view_my_basket')
    else:
        form = BasketAddForm() 

    return render(request, 'basket/add_to_basket.html', {'form': form})

@login_required
def view_my_basket(request):
    if request.user.role != 'customer':
        return redirect('home')
    
    baskets = Basket.objects.filter(customer=request.user).order_by('-created_at')
    return render(request, 'basket/my_basket.html', {'baskets': baskets})

@login_required
def my_purchase_history(request):
    if request.user.role != 'customer':
        return redirect('home')

    purchases = Basket.objects.filter(customer=request.user, status='approved').order_by('-created_at')
    return render(request, 'basket/purchase_history.html', {'purchases': purchases})

@login_required
@user_passes_test(is_staff)
def view_all_baskets(request):
    baskets = Basket.objects.all().order_by('-created_at')
    return render(request, 'basket/all_baskets.html', {'baskets': baskets})

@login_required
@user_passes_test(is_staff)
def update_basket_status(request, pk, action):
    basket = Basket.objects.get(pk=pk)
    if action == 'approve':
        basket.status = 'approved'
    elif action == 'deny':
        basket.status = 'denied'
    basket.save()
    return redirect('view_all_baskets')