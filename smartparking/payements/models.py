from django.db import models
from parking.models import Booking
from django.contrib.auth.models import User
# Create your models here.

class Transaction(models.Model):
    owner         =models.ForeignKey(User,on_delete=models.CASCADE)
    booking       =models.OneToOneField(Booking,on_delete=models.CASCADE)
    transaction_ref = models.CharField(max_length=280,blank=True)
    transaction_id =models.CharField(max_length=280,blank=True)
    charged_amount =models.CharField(max_length=200,blank=True)
    made_on     = models.DateTimeField(auto_now_add=True)


    def __str__(self):

        return f"Transactions for {self.owner.username}"