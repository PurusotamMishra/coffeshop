from django.shortcuts import render
from menu.models import CakeMenu, CoffeeMenu, TeaMenu

# Create your views here.
def  coffee(response):

    coffee = CoffeeMenu.objects.all()

    return render(response, 'coffee.html', {'coffee': coffee})


def  tea(response):

    tea = TeaMenu.objects.all()

    return render(response, 'tea.html', {'tea' : tea})


def  cake(response):

    cake = CakeMenu.objects.all()

    return render(response, 'cake.html', {'cake' : cake})