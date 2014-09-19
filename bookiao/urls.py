from django.conf.urls import include, url

from rest_framework import routers

from core import views

router = routers.DefaultRouter()
router.register(r'businesses', views.BusinessViewSet)
router.register(r'employees', views.EmployeeViewSet)
router.register(r'clients', views.ClientViewSet)
router.register(r'services', views.ServiceViewSet)
router.register(r'appointments', views.AppointmentViewSet)

# Wire up our API using automatic URL routing
# Additionally, we include login URLs for the browseable API
urlpatterns = [
  url(r'^', include(router.urls)),
  url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]