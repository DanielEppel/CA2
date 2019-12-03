from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Voucher(models.Model):
    code = models.CharField(max_length=50, unique=True)
    valid_form = models.DateTimeField()
    valid_to = models.DateTimeField()
    discount = models.IntegerField(validators=[MinValueValidator(0),
                                    MaxValueValidator(100)])

    active = models.BooleanField()


def __str__(self):
    return self.code

# Create your models here.