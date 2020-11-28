
from django.urls import path
from useraccounts import views

app_name="useraccounts"
urlpatterns = [    
    path('register/', views.register,name="register"),
    path('login/', views.login,name="login"),
    path('logout/', views.logout,name="logout"),
    path("user-profile/",views.user_profile,name="user_profile")
]