from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from kudos.models import Kudo
from kudos.permissions import (
    SenderAndReceiverAreDifferent,
    SenderAndReceiverHaveSameOrganization,
    SenderHasKudosAvailable,
    UserAndSenderAreSame,
    UserIsSender,
)
from kudos.serializers import (
    KudoCreateSerializer,
    KudoDetailSerializer,
    KudoListSerializer,
)


class KudoViewSet(ModelViewSet):

    queryset = Kudo.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["by_user", "to_user"]

    def get_permissions(self):
        permission_classes = [IsAuthenticated]

        if self.action == "create":
            permission_classes = [
                IsAuthenticated,
                UserAndSenderAreSame,
                SenderHasKudosAvailable,
                SenderAndReceiverAreDifferent,
                SenderAndReceiverHaveSameOrganization,
            ]

        if self.action in ["update", "partial_update", "destroy"]:
            permission_classes = [
                IsAuthenticated,
                UserIsSender,
            ]

        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        if self.action == "create":
            return KudoCreateSerializer

        if self.action == "retrieve":
            return KudoDetailSerializer

        return KudoListSerializer
