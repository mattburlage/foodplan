from django.shortcuts import render, redirect

from planning.models import Meal, Delivery


def index(request):
    context = {
        'active_meals': Meal.objects.filter(arrived=True, consumed=False, expired=False),
        'deliveries': Delivery.objects.filter()
    }
    return render(request, 'planning/index.html', context)


def meal(request, meal_id):
    context = {
        'meal': Meal.objects.get(pk=meal_id),
    }
    return render(request, 'planning/meal.html', context)
