
from django.urls import path
from parking import views


urlpatterns = [    
    path('', views.home,name="home"),
    path('parkingslots/<int:pk>/',views.parkingslots,name="parkingslots"),
    path('parkingslots/<int:pk>/bookslot/', views.bookslot,name="book_slot"),
    path("bookingslot/booking-comfirm/",views.comfirm_booking,name="comfirm_booking"),
     path("parkingslots/active-slots/",views.active_slots,name="active_slots"),
    path("bookingslot/booking-expired/",views.booking_expired,name="booking_expired"),
]