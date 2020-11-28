from django.db.models.signals import post_save
from django.dispatch import receiver
from parking.models import Booking,ParkingSlot


@receiver(post_save, sender=Booking)
def my_handler(sender, created,instance,**kwargs):

    if not created:
        
        if instance.slot_id:
            slot = ParkingSlot.objects.get(pk=instance.slot_id)
            slot.booked = not slot.booked
            slot.save()
