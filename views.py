# accounts/views.py
from django.shortcuts import render, redirect  # new
from django.http import HttpResponse
from .models import *

from .forms import OrderForm


def home(request):
    # models
    orders = Order.objects.all()
    customers = Customer.objects.all()

    # queries
    total_customers = customers.count()
    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    # context objects
    context = {'orders': orders, 'customers': customers,
               'total_orders': total_orders, 'delivered': delivered, 'pending': pending
               }

    return render(request, 'accounts/dashboard.html', context)


def products(request):
    # models
    products = Product.objects.all()

    return render(request, 'accounts/products.html', {'products': products})


def customer(request, pk):
    # models
    customer = Customer.objects.get(id=pk)

    # queries
    orders = customer.order_set.all()
    order_count = orders.count()

    # context objects
    context = {'customer': customer,
               'orders': orders, 'order_count': order_count}

    return render(request, 'accounts/customer.html', context)


def createOrder(request):
    # formset
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('/')  # home

    # context objects
    context = {'form': form}
    return render(request, 'accounts/order_form.html', context)


def updateOrder(request, pk):
    # queries
    order = Order.objects.get(id=pk)

    # formset
    form = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid:
            form.save()
            return redirect('/')  # home

    # context objects
    context = {'form': form}
    return render(request, 'accounts/order_form.html', context)


def deleteOrder(request, pk):
    # queries
    order = Order.objects.get(id=pk)

    # context objects
    context = {'item': order}
    return render(request, 'accounts/delete.html', context)
