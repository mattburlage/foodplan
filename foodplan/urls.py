from django.contrib import admin
from django.urls import path

from planning import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('meal/<int:meal_id>', views.meal, name='meal'),
]
