from rest_framework import permissions


class IsSenderOrRecepient(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Read-only permissions for sender or receiver
        is_sender_or_receiver = obj.user_from == request.user or obj.user_to == request.user
        if is_sender_or_receiver and request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions for sender only
        return obj.user_from == request.user
