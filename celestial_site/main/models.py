from django.db import models
from django.urls import reverse


class Celestial(models.Model):
    category = models.ForeignKey('Category', related_name='celestial', on_delete=models.PROTECT)
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=50, unique=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    discount = models.DecimalField(max_digits=4, default=0.00, decimal_places=2)
    created =  models.TimeField(auto_now_add=True)
    updated = models.TimeField(auto_now=False)
    image = models.ImageField(upload_to='celestial/%Y/%m/%d', blank=True)

    class Meta:
        ordering = ['name']
        indexes = [models.Index(fields=['id', 'slug']), 
                   models.Index(fields=['name'])]

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("main:celestial_list", kwargs={"celestial_slug": self.slug})
    
    def cell_price(self):
        if self.discount:
            return round(self.price - self.price * self.discount / 100, 2)
        return self.price


class Category(models.Model):
    name = models.CharField(max_length=25, unique=True)
    slug = models.SlugField(max_length=25, unique=True)

    class Meta:
        ordering = ['name']
        indexes = [models.Index(fields=['slug'])]
        
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("main:celestial_list", kwargs={"category_slug": self.slug})
    

class Image(models.Model):
    celestial_obj = models.ForeignKey(Celestial, related_name='images', on_delete=models.PROTECT, null=True)
    image = models.ImageField(upload_to='celestial/%Y/%m/%d', blank=True)
    
    def __str__(self):
        return f'{self.celestial_obj.name} - {self.image.name}'
    