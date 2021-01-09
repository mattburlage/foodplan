from django.shortcuts import render

from planning.models import Meal


def index(request):
    context = {
        'active_meals': Meal.objects.filter(status='Received'),
        'selected_meals': Meal.objects.filter(status='On The Way'),
    }
    return render(request, 'planning/index.html', context)
