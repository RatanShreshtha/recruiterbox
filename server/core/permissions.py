from rest_framework.permissions import BasePermission


class ForUserOnly(BasePermission):
    message = "You can only change your own details."

    def has_object_permission(self, request, view, obj):

        return obj == request.user
