from django.db import models

# Create your models here.


class Meal(models.Model):
    """Creting class for meal."""
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    """Meal ingredients."""
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    name = models.TextField(max_length=50)

    def __str__(self):
        return self.name
