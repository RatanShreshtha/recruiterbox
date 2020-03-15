from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from core.models import User
from core.permissions import ForUserOnly
from core.serializers import UserSerializer


class UserViewSet(ListModelMixin, RetrieveModelMixin, UpdateModelMixin, GenericViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = "username"

    def get_queryset(self):
        if self.action == "list":
            return User.objects.filter(
                organization=self.request.user.organization
            ).exclude(id=self.request.user.id)
        return User.objects.filter(id=self.request.user.id)

    def get_permissions(self):
        permission_classes = [IsAuthenticated]

        if self.action in ["update", "partial_update"]:
            permission_classes = [IsAuthenticated, ForUserOnly]

        return [permission() for permission in permission_classes]


class DeleteAuthToken(APIView):
    def get(self, request, format=None):

        if request.user.is_anonymous:
            return Response(
                {"detail": "Authentication token was not provided."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        request.user.auth_token.delete()
        return Response(
            {"detail": "Authentication token deleted.",}, status=status.HTTP_200_OK
        )


class GenerateAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)
        return Response(
            {
                "id": user.id,
                "kudos": user.kudos(),
                "username": user.username,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "email": user.email,
                "token": token.key,
            },
            status=status.HTTP_201_CREATED,
        )
