import pytest
from django.forms.models import model_to_dict

from core.factories import OrganizationFactory, UserFactory
from core.serializers import OrganizationSerializer, UserSerializer

pytestmark = pytest.mark.django_db


class TestOrganizationSerializer:
    def test_serializer_with_empty_data(self):
        serializer = OrganizationSerializer(data={})
        assert not serializer.is_valid()

    def test_serializer_with_valid_data(self):
        organization = OrganizationFactory.build()

        organization_data = model_to_dict(organization)
        serializer = OrganizationSerializer(data=organization_data)
        assert serializer.is_valid()


class TestUserSerializer:
    def test_serializer_with_empty_data(self):
        serializer = UserSerializer(data={})
        assert not serializer.is_valid()

    def test_serializer_with_valid_data(self):
        organization = OrganizationFactory.build()
        user = UserFactory.build(organization=organization)

        organization_data = model_to_dict(organization)
        user_data = model_to_dict(user)

        user_data["organization"] = organization_data
        serializer = UserSerializer(data=user_data)

        assert serializer.is_valid()
