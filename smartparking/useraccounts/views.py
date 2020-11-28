from django.shortcuts import render,reverse,redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from .forms import CustomUserCreationForm
from django.contrib.auth.models import User
import json

def register(request):
    if request.method == 'POST':

        f = CustomUserCreationForm(request.POST)

        if f.is_valid():

            f.save()
            
            payload ={
                "status":"success",
                "message":"Account created successfully",
                "redirect":reverse("home")
            }

            return JsonResponse(payload,status=201,safe=False)

        else:
            payload={

                "status":"failed",
                "errors":json.dumps(f.errors)
            }

            return JsonResponse(payload,safe=False)




def login(request):

    if request.user.is_authenticated:
        payload={
            "status":"success",
            "message":"Already signed in"
        }

        return JsonResponse(payload,status=200,safe=False)

    if request.method == 'POST':
        
        username = request.POST.get('username')
        password = request.POST.get('password')

        
        user = auth.authenticate(username=username, password=password)
        print(user)

        if user is not None:
            # correct username and password login the user
            auth.login(request, user)
            payload={

                "status":"success",
                "redirect":reverse("home"),
                "message":"Successfully signed in"
            }

            return JsonResponse(payload,status=200,safe=False)

        else:
            payload={

                "status":"failed",
                "message":"Invalid password/email please try again"
            }

            return JsonResponse(payload,safe=False)




def logout(request):
    auth.logout(request)

    payload={
        "status":"success",
        "redirect":reverse("home"),
        "message":"Signed out successfully"
    }

    return JsonResponse(payload,status=200,safe=False)

@login_required
def user_profile(request):

    user = request.user
    bookings = user.booking_set.all()
    transactions = user.transaction_set.all()

    context = {

        "bookings":bookings,
        "transactions":transactions
    }

    print(bookings)
    print(transactions)

    return render(request,"useraccounts/user_account.html",context)




def logout(request):
    auth.logout(request)

    payload={
        "status":"success",
        "redirect":reverse("home"),
        "message":"Signed out successfully"
    }

    return JsonResponse(payload,status=200,safe=False)


