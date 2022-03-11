from rest_framework import permissions


class AnonPermissionOnly(permissions.BasePermission):
    message = "You are already authenicated"
    """
    Non-authenticated users only
    """

    def has_permission(self, request, view):
        return not request.user.is_athenticated


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Object-level
    """

     def has_object_permission(self, request, view, obj):
         if request.method in permissions.SAFE_METHODS:
             return True

         return obj.usern == request.user