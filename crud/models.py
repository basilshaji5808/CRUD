from django.db import models


# Create your models here.
class Application(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=600)
    phone_number = models.CharField(max_length=100)
    email_id = models.EmailField(max_length=100)
    nationality = models.CharField(max_length=200)

    def __str__(self):
        return self.name
