from django.shortcuts import render

from .models import Pizza


# Create your views here.
def home_page(request):
    return render(request, 'pizzerias/home_page.html')


def pizzas(request):
    """Show all pizzas"""
    pizzas = Pizza.objects.order_by('id')
    context = {'pizzas': pizzas}
    return render(request, 'pizzerias/pizzas.html', context)


def pizza(request, pizza_id):
    """Showing topping for the particular pizza."""
    pizza = Pizza.objects.get(id=pizza_id)
    toppings = pizza.topping_set.all()
    context = {'pizza': pizza, 'toppings': toppings}
    return render(request, 'pizzerias/pizza.html', context)
