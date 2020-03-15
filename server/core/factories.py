import factory
from django.utils import timezone

from core.models import Organization, User


class OrganizationFactory(factory.DjangoModelFactory):
    name = factory.Faker("company")
    description = factory.Faker("text")
    date_created = factory.Faker("date_time", tzinfo=timezone.get_current_timezone())

    class Meta:
        model = Organization


class UserFactory(factory.DjangoModelFactory):

    username = factory.Sequence(lambda n: f"testuser{n}")
    password = password = factory.PostGenerationMethodCall(
        "set_password", "qazwsxedc123!@#RFV"
    )
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    email = factory.LazyAttribute(
        lambda u: f"{u.first_name}.{u.last_name}@example.com".lower().replace(" ", "")
    )
    bio = factory.Faker("text")
    organization = factory.SubFactory(OrganizationFactory)
    is_active = True
    is_staff = False

    class Params:
        admin = factory.Trait(is_staff=True, is_superuser=True)

    class Meta:
        model = User
        django_get_or_create = ("username",)
