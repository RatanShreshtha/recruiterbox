from datetime import datetime

from django.conf import settings
from django.shortcuts import get_object_or_404
from rest_framework.permissions import BasePermission

from core.models import User
from kudos.models import Kudo


class UserAndSenderAreSame(BasePermission):
    message = "You can not give kudo as someone else."

    def has_permission(self, request, view):
        return request.data["by_user"] == request.user.id


class UserIsSender(BasePermission):
    message = "You can not update kudo given by someone else."

    def has_object_permission(self, request, view, obj):
        return obj.by_user == request.user


class SenderAndReceiverAreDifferent(BasePermission):
    message = "You can not give kudo to yourself."

    def has_permission(self, request, view):
        return request.data["by_user"] != request.data["to_user"]


class SenderAndReceiverHaveSameOrganization(BasePermission):
    message = "You can not give kudo to someone who is not part your organization."

    def has_permission(self, request, view):
        by_user_org = get_object_or_404(User, pk=request.data["by_user"])
        to_user_org = get_object_or_404(User, pk=request.data["to_user"])

        return by_user_org.organization == to_user_org.organization


class SenderHasKudosAvailable(BasePermission):

    message = "No kudos are available for the month."

    def has_permission(self, request, view):

        month_starting = datetime.today().replace(
            day=1, hour=0, minute=0, second=0, microsecond=0
        )
        kudos_this_month = (
            Kudo.objects.filter(by_user=request.user)
            .filter(awarded__gte=month_starting)
            .count()
        )
        return bool(settings.KUDOS_MONTHLY_QUOTA - kudos_this_month)
