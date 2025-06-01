from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework import permissions


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user.is_authenticated and request.user.user_role == 'admin'
