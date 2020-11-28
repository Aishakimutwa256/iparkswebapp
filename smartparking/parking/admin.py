from django.contrib import admin
from .models import ParkingGround,ParkingSlot,Booking
# Register your models here.

admin.site.site_header = 'IPARKS Administration'
admin.site.site_title = 'Iparks Site'
admin.site.index_title= 'Intelligent Parking System Admin Pannel'

class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'booked_on','slot_id','number_plate','phone_number','car_model','start_time','end_time','booking_id')
    date_hierarchy = 'booked_on'
    list_filter = ['user','booked_on']




admin.site.register(ParkingGround)
admin.site.register(ParkingSlot)
admin.site.register(Booking,BookingAdmin)