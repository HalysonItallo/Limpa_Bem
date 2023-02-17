from django.contrib import admin
from django.urls import path, include
from services.views import ServiceAllUsersViewSet, ServiceManagerViewSet
from attendants.views import AttendantManagerViewSet
from clients.views import ClientAttendantViewSet
from status.views import StatusAttendantViewSet
from customer_service.views import CustomerServiceAttendantViewSet, CustomerServiceHelperViewSet

from rest_framework import routers
from rest_framework.authtoken.views import ObtainAuthToken

router = routers.DefaultRouter()

#Helper Permission
router.register(r'helper/customer-service', CustomerServiceHelperViewSet)

#Geral Permisison 
router.register(r'services', ServiceAllUsersViewSet)

#Attendants Permission
router.register(r'attendants/customer-service', CustomerServiceAttendantViewSet)
router.register(r'attendants/clients', ClientAttendantViewSet)
router.register(r'attendants/status', StatusAttendantViewSet)

#Manager Permission
router.register(r'manager/attendants', AttendantManagerViewSet)
router.register(r'manager/services', ServiceManagerViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('login/', ObtainAuthToken.as_view())
]
