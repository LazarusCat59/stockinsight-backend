from django.urls import path, re_path, include
from . import views

from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views as drf_views

router = DefaultRouter()

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/login/', drf_views.obtain_auth_token),
    re_path(r'api/stock/(?P<pk>[0-9]*)/', views.StockRUDView.as_view()),
    re_path(r'api/stocktype/(?P<pk>[0-9]*)/', views.StockTypeRUDView.as_view()),
    re_path(r'api/audit/(?P<pk>[0-9]*)/', views.AuditDetailsRUDView.as_view()),
    re_path(r'api/stock_create/', views.StockCreateView.as_view()),
    re_path(r'api/stocktype_create/', views.StockTypeCreateView.as_view()),
    re_path(r'api/audit_create/', views.AuditDetailsCreateView.as_view()),
    path('api/stock_list/', views.StockListView.as_view()),
    path('api/stocktype_list/', views.StockTypeListView.as_view()),
    path('api/auditdetails_list/', views.AuditDetailsListView.as_view()),
    path('api/stock_search/', views.StockSearchView.as_view()),
    path('api/stocktype_search/', views.StockTypeSearchView.as_view()),
]
