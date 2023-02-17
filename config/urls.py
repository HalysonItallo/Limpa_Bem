from django.contrib import admin
from django.urls import path, include
from services.views import ServicesViewSet
from attendants.views import AttendantViewSet
from clients.views import ClientViewSet
from status.views import StatusViewSet
from customer_service.views import CustomerServiceAttendantViewSet, CustomerServiceHelperViewSet

from rest_framework import routers
from rest_framework.authtoken.views import ObtainAuthToken

router = routers.DefaultRouter()
router.register(r'services', ServicesViewSet)
router.register(r'helper/customer-service', CustomerServiceHelperViewSet)
router.register(r'attendants/customer-service', CustomerServiceAttendantViewSet)
router.register(r'attendants', AttendantViewSet)
router.register(r'clients', ClientViewSet)
router.register(r'status', StatusViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('login/', ObtainAuthToken.as_view())
]
