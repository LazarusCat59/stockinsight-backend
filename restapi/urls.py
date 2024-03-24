from django.urls import path, include
from . import views

from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views as drf_views

router = DefaultRouter()
router.register(r'stock', views.StockViewSet)
router.register(r'stockcondition', views.StockTypeViewSet)
router.register(r'auditdetails', views.AuditDetailsViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('login/', drf_views.obtain_auth_token),
]
