from django.conf.urls import include, url

from rest_framework import routers

from core import views

router = routers.DefaultRouter()
router.register(r'businesses', views.BusinessViewSet)
router.register(r'employees', views.EmployeeViewSet)
router.register(r'clients', views.ClientViewSet)
router.register(r'services', views.ServiceViewSet)
router.register(r'appointments', views.AppointmentViewSet)
router.register(r'betaemails', views.BetaEmailsViewSet)

# Wire up our API using automatic URL routing
# Additionally, we include login URLs for the browseable API
urlpatterns = [
  url(r'^', include(router.urls)),
  url(r'^register/', 'core.views.register'),
  url(r'^user-type/', 'core.views.user_type'),
  url(r'^available-times/', 'core.views.available_times'),
  url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
  url(r'^api-token-auth/', 'rest_framework_jwt.views.obtain_jwt_token'),
]