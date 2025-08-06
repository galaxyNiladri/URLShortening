from django.db import models

# Create your models here.
class URLStore(models.Model):
    input_url = models.CharField(max_length=500,unique=True)
    hash_url = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"{self.input_url} is shortened to {self.hash_url}"

