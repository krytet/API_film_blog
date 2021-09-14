from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'admin'


class IsModerator(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'moderator'


class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'admin' or request.method in SAFE_METHODS


class IsAuthorOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user or request.method in SAFE_METHODS


class IsAuthorOrModeratorOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        return (
            obj.author == request.user or 
            request.user.role in ['moderator', 'admin'] or
            request.method in SAFE_METHODS
        )



















          