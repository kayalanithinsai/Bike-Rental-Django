from django.db import models
from django.contrib.auth.models import User
import datetime
class branches(models.Model):
    branch_id=models.AutoField(primary_key=True)
    branch_city=models.CharField(max_length=50)
    branch_name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='pics')
    def __str__(self):
        return(str(self.branch_id)+'-'+self.branch_city+'-'+self.branch_name)
class bikes(models.Model):
    bike_id=models.AutoField(primary_key=True)
    bike_company=models.CharField(max_length=50)
    bike_model=models.CharField(max_length=100)
    bike_cost=models.IntegerField()
    bike_availability=models.IntegerField(default=1)
    bike_colour=models.CharField(max_length=30)
    bike_millage=models.IntegerField()
    bike_cc=models.IntegerField(default=0)
    image= models.ImageField( upload_to='bike images')
    branch_id=models.ForeignKey(branches, on_delete=models.CASCADE)
    def __str__(self):
        return (str(self.bike_id)+'. '+self.bike_company+'-'+self.bike_model+'-'+str(self.branch_id)+'-'+self.bike_colour)

class orders(models.Model):
    order_id=models.AutoField(primary_key=True)
    bike_id=models.ForeignKey(bikes, on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    take_time=models.DateTimeField(default=datetime.datetime.now())
    give_time=models.DateTimeField(default= datetime.datetime.now())
    cost=models.IntegerField(default=0)
