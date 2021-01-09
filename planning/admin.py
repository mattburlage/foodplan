from django.contrib import admin

from planning.models import MealService, Delivery, Meal

admin.site.register(MealService)
admin.site.register(Delivery)
admin.site.register(Meal)
