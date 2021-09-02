from django.db import models
class reg(models.Model):
    username=models.CharField(default=True,max_length=100)
    name=models.CharField(max_length=100)
    mobile=models.IntegerField()
    email=models.EmailField()
    password=models.CharField(max_length=100)

    def __str__(self):
        return '{}'.format(self.name)

# Create your models here.
