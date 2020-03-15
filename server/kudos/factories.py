import random

import factory
from django.utils import timezone

from core.factories import UserFactory
from kudos.models import Kudo


class KudoFactory(factory.django.DjangoModelFactory):

    title = factory.Faker("sentence", nb_words=random.randint(6, 14))
    description = factory.Faker("text")
    awarded = factory.Faker("date_time", tzinfo=timezone.get_current_timezone())

    by_user = factory.SubFactory(UserFactory)
    to_user = factory.SubFactory(UserFactory)

    class Meta:
        model = Kudo
