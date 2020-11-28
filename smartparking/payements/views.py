from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from parking.models import Booking,ParkingSlot
from .models import Transaction
from .utils import send_text
import requests
import json


SEC_KEY="FLWSECK_TEST-5b75a3466b76f32f67b02d82aad93b3c-X"
# Create your views here.
def payements(request):

    return render(request,"payements/paypalform.html")


@login_required
def verify_payement(request):


    transaction_id=request.GET.get("transaction_id")
   
    url = f"https://api.flutterwave.com/v3/transactions/{transaction_id}/verify"

    headers= {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {SEC_KEY}'
    }

    response = requests.get(url,headers=headers)
    print(response)
    data = response.json()["data"]
    print(data)
  
    bookings_details = request.session.get("bookings_data")
    
    
    if bookings_details is not None:
        user         = request.user
        car_model    =bookings_details["car_model"]
        number_plate =bookings_details["number_plate"]
        slot_id      =bookings_details["slot_id"]
        end_time     =bookings_details["end_time"]
        start_time   =bookings_details["start_time"]
       
        charged_amount=data["charged_amount"]
        transaction_ref =data["tx_ref"]

        slot =ParkingSlot.objects.get(pk=slot_id)
                                               
        if ((data['status']=="successful") and (int(data["charged_amount"])==int(slot.fee)) and (data["currency"]=="UGX")):
           
            booking,created = Booking.objects.get_or_create(booking_id=transaction_id)

            if created:
                booking.user = request.user
                booking.car_model=car_model
                booking.number_plate=number_plate
                booking.slot_id=int(slot_id)
                booking.start_time=start_time
                booking.end_time=end_time
                booking.phone_number =data["customer"]["phone_number"]
                booking.email = request.user.email
                booking.save()
                
                request.session["booking_period"] = booking.time_period
                request.session["booking_id"] =booking.booking_id

                transaction = Transaction.objects.create(owner=booking.user,booking=booking,
                                                            charged_amount=charged_amount,
                                                            transaction_id=transaction_id,
                                                            transaction_ref=transaction_ref,
                                                            )

                transaction.save()
                del request.session['bookings_data']

                phone_number =data["customer"]["phone_number"].replace(data["customer"]["phone_number"][0:1],'+256',1)
               
                request.session["phone_number"] = phone_number
                send_text(phone_number,"Your Slot has been booked,Thank you for using iparks",request=request)
                messages.success(request, 'Congs, your slot has been successfully booked for you')

        else:

            del request.session['bookings_data']

            messages.error(request, 'Oops!! something went wrong, please comfirm the right amount charged for slot')
           

    elif bookings_details is None:
   
        messages.error(request, 'Please fill in your booking credentials for booking again')
    
    return render(request,"payements/verify_transaction.html")