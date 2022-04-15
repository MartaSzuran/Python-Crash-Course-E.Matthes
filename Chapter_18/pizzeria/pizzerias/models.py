from django.db import models

# Create your models here.


class Pizza(models.Model):
    """Creating specific pizza."""
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Topping(models.Model):
    """Pizza toppings."""
    pizza = models.ForeignKey(Pizza, on_delete=models.DO_NOTHING)
    name = models.TextField()

    class Meta:
        verbose_name_plural = "toppings"

    def __str__(self):
        return self.name
