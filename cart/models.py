
from home.models import *

class cart_list(models.Model):
    cart_id=models.CharField(max_length=23,unique=True)
    date_add=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.cart_id

class item(models.Model):
    prodt=models.ForeignKey(product,on_delete=models.CASCADE)
    cart=models.ForeignKey(cart_list,on_delete=models.CASCADE)
    quan=models.IntegerField()
    active=models.BooleanField(default=True)

    class Meta:
        ordering = ('prodt',)
        verbose_name = 'item'
        verbose_name_plural = 'items'

    def __str__(self):
        return '{}'.format(self.prodt)
    def iprice(self):
        return self.prodt.price*self.quan