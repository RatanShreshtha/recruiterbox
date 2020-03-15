import pytest

from core.factories import OrganizationFactory, UserFactory
from kudos.factories import KudoFactory

pytestmark = pytest.mark.django_db


def test_kudo_model():
    organization = OrganizationFactory()
    by_user = UserFactory(organization=organization)
    to_user = UserFactory(organization=organization)
    kudo = KudoFactory(by_user=by_user, to_user=to_user)

    assert kudo.__str__() == f"{kudo.title}"
