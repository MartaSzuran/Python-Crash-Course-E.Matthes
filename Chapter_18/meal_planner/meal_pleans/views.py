from django.shortcuts import render

# Create your views here.


def home_page(request):
    """Home page for App meal_plan."""
    return render(request, 'meal_pleans\home_page.html')
