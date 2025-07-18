from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    isbn = models.CharField(max_length=13, unique=True)
    published_date = models.DateField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.title