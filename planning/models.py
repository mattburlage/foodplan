from django.db import models
from django.utils import timezone


class MealService(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Delivery(models.Model):
    service = models.ForeignKey(MealService, on_delete=models.CASCADE)
    arrival = models.DateField()

    def __str__(self):
        return f'{self.service.name} on {self.arrival.strftime("%x")}'


MEAL_STATUS_CHOICES = [
    (0, 'On The Way'),
    (1, 'Received'),
    (2, 'Consumed'),
]


class Meal(models.Model):
    name = models.CharField(max_length=64)
    status = models.CharField(max_length=12, choices=MEAL_STATUS_CHOICES, default=1)
    eat_by = models.DateField(null=True, blank=True)

    @staticmethod
    def active_meals():
        return Meal.objects.filter(eat_by_gte=timezone.now().date(), status=1)

    def __str__(self):
        return f'{self.name}'
