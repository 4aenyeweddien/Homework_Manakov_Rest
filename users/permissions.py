from rest_framework.permissions import BasePermission


class IsModerator(BasePermission):
    """Проверка, является ли пользователь модератором."""

    def has_permission(self, request, view):
        return request.user.groups.filter(name='moderators').exists()

    def has_object_permission(self, request, view, obj):
        return request.user.groups.filter(name='moderators').exists()


class IsOwner(BasePermission):
    """Проверка, является ли пользователь владельцем"""

    def has_object_permission(self, request, view, obj):
        if obj.owner == request.user:
            return True
        return False