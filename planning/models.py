from django.contrib.auth.models import User
from django.db import models
from django.db.models import Sum
from django.utils import timezone


class MealService(models.Model):
    name = models.CharField(max_length=32)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name


class Delivery(models.Model):
    service = models.ForeignKey(MealService, on_delete=models.CASCADE)
    arrival = models.DateField()
    arrived = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.service.name} on {self.arrival.strftime("%x")}'

    def serving_count(self):
        return self.meals.aggregate(s=Sum('servings'))['s']

    class Meta:
        verbose_name_plural = "Deliveries"


MEAL_STATUS_CHOICES = [
    ('On The Way', 'On The Way'),
    ('Received', 'Received'),
    ('Consumed', 'Consumed'),
    ('Expired', 'Expired'),
]


class MealStatusChoice(models.Model):
    label = models.CharField(max_length=32)

    def __str__(self):
        return self.label


class Meal(models.Model):
    name = models.CharField(max_length=64)
    delivery = models.ForeignKey(Delivery, on_delete=models.CASCADE, related_name='meals')

    arrived = models.BooleanField(default=False)
    consumed = models.BooleanField(default=False)
    expired = models.BooleanField(default=False)

    servings = models.IntegerField(default=1)

    eat_by = models.DateField()

    notes = models.TextField(null=True, blank=True)

    @staticmethod
    def active_meals(active_date=None):
        return Meal.objects.filter(eat_by_gte=active_date, status=1)

    def status(self):
        if self.expired:
            return 'Spoiled'
        elif not self.arrived:
            return 'On The Way'
        elif not self.consumed:
            return 'In Fridge'
        else:
            return 'Consumed'

    def service(self):
        return self.delivery.service

    def __str__(self):
        return f'{self.name}'
