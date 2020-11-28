from twilio.rest import Client
from django.shortcuts import redirect
from twilio.twiml.voice_response import VoiceResponse
from django.conf import settings
from django.contrib import messages



def send_text(phone_number,iparks_message,request):
    # create twilio client using account ssid and auth token
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

    # create message
    try:
        message = client.messages.create(
            to= phone_number, 
            from_=settings.TRIAL_NUMBER, # insert trial number 
            body=iparks_message) # insert message

        print("I am in sending message")
    except:
        messages.error(request, 'please contact us when you see this')
        
        return redirect("payements:transaction_complete")
    return None


