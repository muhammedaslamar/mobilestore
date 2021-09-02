from django.db import models
from django.urls import reverse

class categ(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    def get_url(self):
        return reverse('cat_prod',args=[self.slug])
    def __str__(self):
        return '{}'.format(self.name)
class product(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    img=models.ImageField(upload_to="product")
    desc=models.TextField(max_length=1000)
    stock=models.IntegerField()
    available=models.BooleanField()
    price=models.IntegerField()
    category=models.ForeignKey(categ,on_delete=models.CASCADE)


    def get_url(self):
        return reverse('pro',args=[self.category.slug,self.slug])



    class Meta:
        ordering=('name',)
        verbose_name='product'
        verbose_name_plural='products'

    def __str__(self):
        return '{}'.format(self.name)
# Create your models here.
