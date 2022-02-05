from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS


class CustomPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method not in SAFE_METHODS:
            return obj.author == request.user
        return True

    def has_permission(self, request, view):
        return request.user.is_authenticated
