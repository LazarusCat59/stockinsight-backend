from rest_framework.permissions import BasePermission, SAFE_METHODS

class AuditorOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        
        return (request.user.role == 'ADT') | (request.user.role == 'HOD')

class CustodianOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        
        return (request.user.role == 'CDN') | (request.user.role == 'HOD')

class IsHOD(BasePermission):
    def has_permission(self, request, view):
        return (request.user.role == 'HOD')

class IsAuditor(BasePermission):
    def has_permission(self, request, view):
        return (request.user.role == 'ADT') | (request.user.role == 'HOD')

class IsCustodian(BasePermission):
    def has_permission(self, request, view):
        return (request.user.role == 'CDN') | (request.user.role == 'HOD')
