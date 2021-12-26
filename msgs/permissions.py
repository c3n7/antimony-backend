from rest_framework import permissions


class IsSenderOrRecepient(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user_from == request.user or obj.user_to == request.user
