from django.db import models

class AbstractItem(models.Model):
    name = models.CharField(max_length=50, default="", blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

class Category(AbstractItem):
    pass

class Content(models.Model):
    title = models.CharField(max_length=50, blank=True)
    description = models.TextField(blank=True)
    category = models.ManyToManyField(Category, related_name='posts', blank=True)

    def __str__(self):
        return self.title