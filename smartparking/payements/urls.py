from django.urls import path
from payements import views

app_name="payements"

urlpatterns = [    
    path('', views.payements,name="payements_form"),
    path("transaction-complete/",views.verify_payement,name="transaction_complete")
]