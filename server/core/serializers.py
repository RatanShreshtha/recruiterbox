from rest_framework.serializers import ModelSerializer, IntegerField

from core.models import Organization, User


class OrganizationSerializer(ModelSerializer):
    class Meta:
        model = Organization
        fields = ["name", "description"]


class UserSerializer(ModelSerializer):
    organization = OrganizationSerializer()

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "bio",
            "organization",
        ]
        lookup_field = "username"
