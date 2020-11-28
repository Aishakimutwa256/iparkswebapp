from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from parking import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('parking.urls')),
    path('payements/',include('payements.urls',namespace="payements")),
    path('useraccounts/',include('useraccounts.urls',namespace="useraccounts")),
 
]


if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)