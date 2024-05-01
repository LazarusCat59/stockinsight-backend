from django.urls import path, re_path, include
from . import views

from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views as drf_views

urlpatterns = [
    path('api/login/', drf_views.obtain_auth_token),
    path('api/register/', views.CreateUserView.as_view()),
    re_path(r'api/stock/(?P<pk>[0-9]*)/', views.StockRUDView.as_view(), name='stock-detail'),
    re_path(r'api/computer/(?P<pk>[0-9]*)/', views.ComputerRUDView.as_view(), name='computer-detail'),
    re_path(r'api/stocktype/(?P<pk>[0-9]*)/', views.StockTypeRUDView.as_view(), name='stocktype-detail'),
    re_path(r'api/audit/(?P<pk>[0-9]*)/', views.AuditDetailRUDView.as_view(), name='audit-detail'),
    path(r'api/stock_create/', views.StockCreateView.as_view(), name='stock-create'),
    path(r'api/computer_create/', views.StockCreateView.as_view(), name='computer-create'),
    path(r'api/stocktype_create/', views.StockTypeCreateView.as_view(), name='stocktype-create'),
    path(r'api/audit_create/', views.AuditDetailCreateView.as_view(), name='audit-create'),
    path('api/stock_list/', views.StockListView.as_view(), name='stock-list'),
    path('api/computer_list/', views.StockListView.as_view(), name='computer-list'),
    path('api/stocktype_list/', views.StockTypeListView.as_view(), name='stocktype-list'),
    path('api/audit_list/', views.AuditDetailListView.as_view(), name='audit-list'),
    path('api/stock_search/', views.StockSearchView.as_view(), name='stock-search'),
    path('api/stocktype_search/', views.StockTypeSearchView.as_view(), name='stocktype-search'),
    path('api/user/', views.GetUserView.as_view(), name='user-detail'),
]
