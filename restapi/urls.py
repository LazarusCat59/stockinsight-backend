from django.urls import path, re_path, include
from . import views

from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views as drf_views

urlpatterns = [
    path('api/login/', drf_views.obtain_auth_token),
    path('api/register/', views.CreateUserView.as_view()),
    re_path(r'api/stock/(?P<pk>[0-9]*)/', views.StockRUDView.as_view(), name='stock-detail'),
    re_path(r'api/computer/(?P<pk>[0-9]*)/', views.ComputerRUDView.as_view(), name='computer-detail'),
    re_path(r'api/audit/(?P<pk>[0-9]*)/', views.AuditDetailRUDView.as_view(), name='audit-detail'),
    re_path(r'api/user/(?P<pk>[0-9]*)/', views.UsersView.as_view(), name='user-detail'),
    re_path(r'api/assignment/(?P<pk>[0-9]*)/', views.AssignmentRUDView.as_view(), name='assignment-detail'),
    path(r'api/stock_create/', views.StockCreateView.as_view(), name='stock-create'),
    path(r'api/computer_create/', views.ComputerCreateView.as_view(), name='computer-create'),
    path(r'api/audit_create/', views.AuditDetailCreateView.as_view(), name='audit-create'),
    path(r'api/assignment_create/', views.AssignmentCreateView.as_view(), name='assignment-create'),
    path('api/stock_list/', views.StockListView.as_view(), name='stock-list'),
    path('api/computer_list/', views.ComputerListView.as_view(), name='computer-list'),
    path('api/audit_list/', views.AuditDetailListView.as_view(), name='audit-list'),
    path('api/assignment_list/', views.AssignmentListView.as_view(), name='assignment-list'),
    path('api/stock_search/', views.StockSearchView.as_view(), name='stock-search'),
    path('api/currentuser/', views.GetCurrentUserView.as_view(), name='currentuser-detail'),
    path('api/locations/', views.GetLocationsView.as_view(), name='locations'),
    path('api/conditions/', views.GetConditionsView.as_view(), name='conditions'),
    path('api/categories/', views.GetCategoriesView.as_view(), name='categories'),
    path('api/auditedstocks/', views.GetAuditedStocksView.as_view(), name='auditedstocks'),
    path('api/unassignedauditors/', views.GetUnassignedAuditorView.as_view(), name='unassignedauditors'),
    path('api/getassignment/', views.GetAssignmentView.as_view(), name='getassignment'),
]
