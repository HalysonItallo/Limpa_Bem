from django.contrib import admin
from django.urls import path, include
from services.views import ServicesViewSet
from customer_service.views import GetAllCustomerService
from attendants.views import AttendantViewSet
from clients.views import ClientViewSet
from status.views import StatusViewSet

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'services', ServicesViewSet)
# router.register(r'customer-service', )
router.register(r'attendants', AttendantViewSet)
router.register(r'clients', ClientViewSet)
router.register(r'status', StatusViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
