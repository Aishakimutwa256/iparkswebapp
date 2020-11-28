from django.db import models
from django.contrib.auth.models import User
from datetime import datetime,timedelta
from PIL import Image
# Create your models here.

class ParkingGround(models.Model):
    name = models.CharField(max_length=200,blank=True)
    image = models.ImageField(upload_to='images/parking_ground/')



    class Meta:
        verbose_name_plural="Parking Grounds"

    def __str__(self):

        return self.name
       
    def save(self):

        super(ParkingGround,self).save()  # saving image first

        img = Image.open(self.image.path) # Open image using self

        if img.height > 300 or img.width > 300:
            new_img = (300, 300)
            img.thumbnail(new_img)
            img.save(self.image.path)







class ParkingSlot(models.Model):
    name = models.CharField(max_length=200,blank=True)
    parking_ground = models.ForeignKey(ParkingGround,on_delete=models.CASCADE)
    fee = models.CharField(max_length=500,blank=True)
    booked = models.BooleanField(blank=False,default=False,null=False)



    class Meta:
        verbose_name_plural="Parking Slots"


    def __str__(self):

        return self.name


class Booking(models.Model):
    user         = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    slot_id      =models.PositiveIntegerField(blank=True,null=True)
    number_plate  =models.CharField(blank=True,null=True,max_length=200)
    phone_number = models.CharField(max_length=200,blank=False, verbose_name ="Phone Number")
    email        =models.CharField(max_length=280,blank=False)
    car_model    =models.CharField(max_length=300,blank=False)
    start_time   = models.CharField(max_length=100,blank=False,verbose_name="Starting Time")
    end_time     = models.CharField(max_length=100,blank=False,verbose_name="Ending Time")
    booking_id   =models.CharField(max_length=200,blank=True)
    booked_on   = models.DateTimeField(auto_now_add =True)
   
    @property
    def time_period(self):
        start = datetime.strptime(str(self.start_time),"%H:%M")
        end =   datetime.strptime(str(self.end_time),"%H:%M")
        time_interval =(end - start)
        total_seconds = time_interval.total_seconds()

        max_period= datetime.now()+ timedelta(seconds=total_seconds) 
 
        return str(max_period)
        
        
        


    def save(self,*args,**kwargs):
        print(self.start_time)
 
        super(Booking,self).save(*args,**kwargs)


    def __str__(self):

        return f"Bookings For  {self.user.username}"