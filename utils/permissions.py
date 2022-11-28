from rest_framework import permissions


class Patch_is_admin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.is_authenticated and request.user.is_superuser


class Patch_is_user(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.is_authenticated and request.user.id == obj.id


class Register_permission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == "POST":
            return True
        return request.user.is_authenticated and request.user.is_superuser


class Get_and_delete_permission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if (
            request.user.is_authenticated
            and request.method == "GET"
            and request.user == obj
        ):
            return True
        return request.user.is_authenticated and request.user.is_superuser
