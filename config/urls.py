from django.contrib import admin
from django.urls import path, include
from services.views import ServiceViewSet
from status.views import StatusAttendantViewSet
from users.views import PersonViewSet
from customer_service.views import CustomerServiceViewSet

from rest_framework import routers
from rest_framework.authtoken.views import ObtainAuthToken

router = routers.DefaultRouter()

router.register(r'customer-service', CustomerServiceViewSet)
router.register(r'services', ServiceViewSet)
router.register(r'persons', PersonViewSet)


## TODO: arrumar o status
router.register(r'attendants/status', StatusAttendantViewSet)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('login/', ObtainAuthToken.as_view())
]
