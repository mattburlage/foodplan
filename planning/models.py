from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class MealService(models.Model):
    name = models.CharField(max_length=32)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name


class Delivery(models.Model):
    service = models.ForeignKey(MealService, on_delete=models.CASCADE)
    arrival = models.DateField()

    def __str__(self):
        return f'{self.service.name} on {self.arrival.strftime("%x")}'

    class Meta:
        verbose_name_plural = "Deliveries"


MEAL_STATUS_CHOICES = [
    ('On The Way', 'On The Way'),
    ('Received', 'Received'),
    ('Consumed', 'Consumed'),
]


class Meal(models.Model):
    name = models.CharField(max_length=64)
    delivery = models.ForeignKey(Delivery, on_delete=models.CASCADE)
    status = models.CharField(max_length=12, choices=MEAL_STATUS_CHOICES, default='On The Way')
    servings = models.IntegerField(default=1)
    eat_by = models.DateField(null=True, blank=True)

    @staticmethod
    def active_meals(active_date=None):
        if not active_date:
            active_date = timezone.now().date()

        return Meal.objects.filter(eat_by_gte=active_date, status=1)

    def service(self):
        return self.delivery.service

    def __str__(self):
        return f'{self.name}'
