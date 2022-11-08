from django.db import models

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=255, blank=False, null=False)
    last_name = models.CharField(max_length=255, blank=False, null=False)

    def __str__(self):
        return self.last_name


class Book(models.Model):
    title = models.CharField(max_length=255, blank=False, null=False)
    length = models.IntegerField()
    author = models.ManyToManyField(Author)

    def __str__(self):
        return self.title


