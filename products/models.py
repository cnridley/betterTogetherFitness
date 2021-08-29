from django.db import models

# Create your models here.


class Gallery(models.Model):

    class Meta:
        verbose_name_plural = "Gallery" # how the model is displayed in the admin page


    name = models.CharField(max_length=254, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    image_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name


class nutritionGuides(models.Model):

    class Meta:
        verbose_name_plural = "Nutrition Guides" # how the model is displayed in the admin page

    title = models.CharField(max_length=254, null=True, blank=True) 
    description = models.TextField(max_length=254, null=True, blank=True)
    price = models.DecimalField(decimal_places=2, null=True, blank=True, max_digits=100)

    def __str__(self):
        return self.title
