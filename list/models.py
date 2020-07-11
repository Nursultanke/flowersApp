from django.db import models


class AllFlowers(models.Model):
    owner_name = models.CharField(max_length=150)
    title = models.CharField(max_length=150)
    price = models.CharField(max_length=150)
    description = models.TextField()
    address = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=150)
    image = models.ImageField(blank=False, null=False)

    def __str__(self):
        return self.title
