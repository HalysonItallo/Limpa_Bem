from django.contrib import admin
from django.urls import path, include
from services.views import ServiceViewSet
from status.views import StatusViewSet
from users.views import PersonViewSet, AuthTokenView
from customer_service.views import CustomerServiceViewSet
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'customer-service', CustomerServiceViewSet)
router.register(r'services', ServiceViewSet)
router.register(r'persons', PersonViewSet)
router.register(r'status', StatusViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('login/', AuthTokenView.as_view())
]
