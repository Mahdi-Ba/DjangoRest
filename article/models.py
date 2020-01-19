from django.db import models


class Writer(models.Model):
    name = models.CharField(max_length=100)
    family = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100, null=True)
    auther = models.ForeignKey(Writer, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
