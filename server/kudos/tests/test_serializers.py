import pytest
from django.forms.models import model_to_dict

from core.factories import OrganizationFactory, UserFactory
from kudos.factories import KudoFactory
from kudos.serializers import (
    KudoCreateSerializer,
    KudoDetailSerializer,
    KudoListSerializer,
)

pytestmark = pytest.mark.django_db


class TestKudoListSerializer:
    def test_serializer_with_empty_data(self):
        serializer = KudoListSerializer(data={})
        assert not serializer.is_valid()

    def test_serializer_with_valid_data(self):
        organization = OrganizationFactory()
        by_user = UserFactory(organization=organization)
        to_user = UserFactory(organization=organization)

        kudo_data = model_to_dict(KudoFactory.build(by_user=by_user, to_user=to_user))
        serializer = KudoListSerializer(data=kudo_data)
        assert serializer.is_valid()


class TestKudoDetailSerializer:
    def test_serializer_with_empty_data(self):
        serializer = KudoDetailSerializer(data={})
        assert not serializer.is_valid()

    def test_serializer_with_valid_data(self):
        organization = OrganizationFactory()
        by_user = UserFactory.build(organization=organization)
        to_user = UserFactory.build(organization=organization)

        organization_data = model_to_dict(organization)
        by_user_data = model_to_dict(by_user)
        to_user_data = model_to_dict(to_user)

        by_user_data["organization"] = organization_data
        to_user_data["organization"] = organization_data

        kudo_data = model_to_dict(KudoFactory.build(by_user=by_user, to_user=to_user))

        kudo_data["by_user"] = by_user_data
        kudo_data["to_user"] = to_user_data
        serializer = KudoDetailSerializer(data=kudo_data)

        assert serializer.is_valid()


class TestKudoCreateSerializer:
    def test_serializer_with_empty_data(self):
        serializer = KudoCreateSerializer(data={})
        assert not serializer.is_valid()

    def test_serializer_with_valid_data(self):
        organization = OrganizationFactory()
        by_user = UserFactory(organization=organization)
        to_user = UserFactory(organization=organization)

        kudo_data = model_to_dict(KudoFactory.build(by_user=by_user, to_user=to_user))
        serializer = KudoCreateSerializer(data=kudo_data)
        assert serializer.is_valid()
