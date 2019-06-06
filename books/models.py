from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100)
    read = models.BooleanField(default=False, null=True, blank=True)
    started_date = models.DateField(null=True, blank=True)
    finished_date = models.DateField(null=True, blank=True)
    rating = models.IntegerField(default=1, null=True, blank=True,
                                 validators=[MaxValueValidator(10), MinValueValidator(1)])
    review = models.TextField(null=True, blank=True, max_length=300)

    class Meta:
        db_table = 'books'
