from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.views.generic import ListView
from .models import  *

def home(request):
    par = {
        'header': 'Home'
    }
    return render(request, 'home.html', context=par)


class CustomerView(ListView):
    model = Customer
    template_name = 'customer_list.html'


class ZakazView(ListView):
    model = zakaz
    template_name = 'zakazs.html'
    context_object_name = 'zakaz_list'


class OrderView(ListView):
    model = Usluga
    template_name = 'order_list.html'
