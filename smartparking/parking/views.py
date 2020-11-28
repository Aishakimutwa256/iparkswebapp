from django.shortcuts import render,redirect,get_object_or_404
from .models import ParkingGround,ParkingSlot,Booking
from django.http import  JsonResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from payements.utils import send_text


# Create your views here.
def home(request):

    parking_grounds = ParkingGround.objects.all()

    return render(request,"parking/home.html",{"parking_grounds":parking_grounds})

def parkingslots(request,pk):

    parking_ground =get_object_or_404(ParkingGround,pk=pk)
    slots = parking_ground.parkingslot_set.all() 

    return render(request,"parking/parkingslots.html",{"slots":slots})

@login_required    
def bookslot(request,**kwargs):

    if request.method=="POST":

        car_model = request.POST.get("car-model")
        number_plate = request.POST.get("number-plate")
        slot_id      = request.POST.get("slot_id")
        start =request.POST.get("start")
        end   = request.POST.get("end")


        bookings_data ={
            "slot_id":slot_id,
            "number_plate":number_plate,
            "car_model":car_model,
            "start_time":start,
            "end_time":end
        }

        
        bookingdata ={
            "redirect":reverse("payements:payements_form"),
            "status":"success",
            "bookings_data":bookings_data
            }

        request.session["bookings_data"] = bookings_data

        return JsonResponse(bookingdata,safe=False, status=200)
    else:

        return JsonResponse({"error":"Only post requests are allowed"})
    

    return HttpResponse("Booking slots")


def comfirm_booking(request):

    context=request.session.get("bookings_data")

    print(context)

    return render(request,"parking/comfirm_booking.html")


def booking_expired(request):
    
    #getting the booking using the booking id
    booking_id = request.session.get("booking_id")
    booking = get_object_or_404(Booking,booking_id=booking_id)

    #get the slot using the slot id of the booking
    slot_id = int(booking.slot_id)
    slot = get_object_or_404(ParkingSlot,pk=slot_id)

    #update the slot retrieved by slot id
    slot.booked = False
    slot.save()
    #send voice message to user
    phone_number = request.session.get("phone_number")
    send_text(phone_number,"Dear customer,Your booking Session has expired. Thank you  for using iparks",request)
    del request.session["phone_number"]
    del request.session["booking_id"]
    
    
    payload={
        "status":"success",
        
    }
    return JsonResponse(payload,status=200,safe=False)


def active_slots(request):



    return render(request,"parking/active_parkingslots.html")
