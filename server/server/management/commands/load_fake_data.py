import random

from django.core.management.base import BaseCommand

from core.factories import OrganizationFactory, UserFactory
from core.models import User
from kudos.factories import KudoFactory


class Command(BaseCommand):
    help = "Create fake data for the application."

    def add_arguments(self, parser):
        parser.add_argument(
            "-o", "--orgs", default=3, type=int, help="Organizations to create",
        )
        parser.add_argument(
            "-k", "--kudos", default=12, type=int, help="Kudos to create"
        )
        parser.add_argument(
            "-u", "--users", default=20, type=int, help="Users to create"
        )

    def handle(self, *args, **kwargs):

        organizations = []
        for _ in range(kwargs["orgs"]):
            organization = OrganizationFactory()
            self.stdout.write(
                self.style.SUCCESS(f"<Organization: name={organization.name}>")
            )
            organizations.append(organization)

        root1 = UserFactory(
            username="root1", organization=organizations[0], admin=True,
        )

        self.stdout.write(
            self.style.SUCCESS(
                f"<User: username={root1.username}, first_name={root1.first_name}, last_name={root1.last_name}, organization={root1.organization}>"
            )
        )

        root2 = UserFactory(
            username="root2", organization=organizations[1], admin=True,
        )

        self.stdout.write(
            self.style.SUCCESS(
                f"<User: username={root2.username}, first_name={root2.first_name}, last_name={root2.last_name}, organization={root2.organization}>"
            )
        )

        users = [root1, root2]
        for _ in range(kwargs["users"] - 2):
            organization = random.choice(organizations)
            user = UserFactory(organization=organization)
            self.stdout.write(
                self.style.SUCCESS(
                    f"<User: username={user.username}, first_name={user.first_name}, last_name={user.last_name}, organization={user.organization}>"
                )
            )
            users.append(user)

        kudos = []
        num_kudos = kwargs["kudos"]

        while num_kudos:
            try:
                by_user = random.choice(users)
                to_users = User.objects.filter(
                    organization=by_user.organization
                ).exclude(username=by_user.username)
                to_user = random.choice(to_users)
                kudo = KudoFactory(by_user=by_user, to_user=to_user)
                self.stdout.write(
                    self.style.SUCCESS(
                        f"<Kudo: by_user={by_user.username}, to_user={to_user.username}, title={kudo.title}>"
                    )
                )
                kudos.append(kudo)
                num_kudos -= 1
            except Exception as e:
                print(e)
                continue
