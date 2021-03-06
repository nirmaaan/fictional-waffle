from rest_framework import routers
from .api import LeadViewSet


router = routers.DefaultRouter()
router.register('api/Leads', LeadViewSet, 'leads')

urlpatterns = router.urls