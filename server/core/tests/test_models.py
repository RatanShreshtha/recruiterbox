import pytest

from core.factories import OrganizationFactory, UserFactory

pytestmark = pytest.mark.django_db


def test_organization_model():
    organization = OrganizationFactory()
    assert organization.__str__() == f"{organization.name}"


def test_user_model():
    user = UserFactory()
    assert user.__str__() == f"{user.first_name} {user.last_name} ({user.username})"
