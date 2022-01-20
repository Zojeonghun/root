from django.db import models

class AbstractItem(models.Model):
    name = models.CharField(max_length=50, default="", blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

class Location(AbstractItem):
    pass


class Workshop(models.Model):
    name = models.CharField(max_length=50, blank=True)
    location = models.ManyToManyField(Location, related_name='workshops', blank=True)
    address = models.CharField(max_length=50, blank=True)
    address_text = models.CharField(max_length=50, blank=True)
    number = models.CharField(max_length=50, blank=True)
    link = models.CharField(max_length=50,blank=True)
    address_x = models.CharField(max_length=50, blank=True)
    address_y = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.name