from datetime import datetime

import pytest
from django.conf import settings
from django.forms.models import model_to_dict
from django.urls import reverse
from rest_framework import status

from core.factories import OrganizationFactory, UserFactory
from kudos.factories import KudoFactory

pytestmark = pytest.mark.django_db


def test_list_kudos(client):
    organization = OrganizationFactory()
    user1 = UserFactory(password="qazwsxedc123!@#RFV", organization=organization)
    user2 = UserFactory(password="qazwsxedc123!@#RFV", organization=organization)

    KudoFactory.create_batch(4, by_user=user1, to_user=user2)
    KudoFactory.create_batch(4, by_user=user2, to_user=user1)

    token_generation_url = reverse("generate-token")

    credentials = {
        "username": user1.username,
        "password": "qazwsxedc123!@#RFV",
    }

    resp = client.post(token_generation_url, data=credentials)
    token = resp.data["token"]

    kudo_list_url = reverse("kudo-list")

    resp = client.get(kudo_list_url, HTTP_AUTHORIZATION=f"Token {token}")
    assert resp.status_code == status.HTTP_200_OK
    assert len(resp.data["results"]) == 8

    KudoFactory.create_batch(4, by_user=user1, to_user=user2)
    KudoFactory.create_batch(4, by_user=user2, to_user=user1)

    resp = client.get(kudo_list_url, HTTP_AUTHORIZATION=f"Token {token}")
    assert resp.status_code == status.HTTP_200_OK
    assert len(resp.data["results"]) == 10


def test_details_kudo(client):
    organization = OrganizationFactory()
    user1 = UserFactory(password="qazwsxedc123!@#RFV", organization=organization)
    user2 = UserFactory(password="qazwsxedc123!@#RFV", organization=organization)

    kudo = KudoFactory(by_user=user1, to_user=user2)

    token_generation_url = reverse("generate-token")

    credentials = {
        "username": user1.username,
        "password": "qazwsxedc123!@#RFV",
    }

    resp = client.post(token_generation_url, data=credentials)
    token = resp.data["token"]

    kudo_detail_url = reverse("kudo-detail", kwargs={"pk": kudo.pk})

    resp = client.get(kudo_detail_url, HTTP_AUTHORIZATION=f"Token {token}")
    assert resp.status_code == status.HTTP_200_OK


def test_update_kudo(client):
    organization = OrganizationFactory()
    user1 = UserFactory(password="qazwsxedc123!@#RFV", organization=organization)
    user2 = UserFactory(password="qazwsxedc123!@#RFV", organization=organization)
    user3 = UserFactory(password="qazwsxedc123!@#RFV", organization=organization)

    kudo = KudoFactory(by_user=user1, to_user=user2)

    token_generation_url = reverse("generate-token")

    credentials = {
        "username": user1.username,
        "password": "qazwsxedc123!@#RFV",
    }

    resp = client.post(token_generation_url, data=credentials)
    token = resp.data["token"]

    kudo_detail_url = reverse("kudo-detail", kwargs={"pk": kudo.pk})

    data = {
        "title": "Kudo Updated",
        "description": "Lorem Ipsum data tum",
        "by_user": user1.id,
        "to_user": user3.id,
    }

    resp = client.put(
        kudo_detail_url,
        data=data,
        HTTP_AUTHORIZATION=f"Token {token}",
        content_type="application/json",
    )
    assert resp.status_code == status.HTTP_200_OK


def test_destroy_kudo(client):
    organization = OrganizationFactory()
    user1 = UserFactory(password="qazwsxedc123!@#RFV", organization=organization)
    user2 = UserFactory(password="qazwsxedc123!@#RFV", organization=organization)

    kudo = KudoFactory(by_user=user1, to_user=user2)

    token_generation_url = reverse("generate-token")

    credentials = {
        "username": user1.username,
        "password": "qazwsxedc123!@#RFV",
    }

    resp = client.post(token_generation_url, data=credentials)
    token = resp.data["token"]

    kudo_detail_url = reverse("kudo-detail", kwargs={"pk": kudo.pk})

    resp = client.delete(
        kudo_detail_url,
        HTTP_AUTHORIZATION=f"Token {token}",
        content_type="application/json",
    )
    assert resp.status_code == status.HTTP_204_NO_CONTENT


def test_partial_update_kudo(client):
    organization = OrganizationFactory()
    user1 = UserFactory(password="qazwsxedc123!@#RFV", organization=organization)
    user2 = UserFactory(password="qazwsxedc123!@#RFV", organization=organization)

    kudo = KudoFactory(by_user=user1, to_user=user2)

    token_generation_url = reverse("generate-token")

    credentials = {
        "username": user1.username,
        "password": "qazwsxedc123!@#RFV",
    }

    resp = client.post(token_generation_url, data=credentials)
    token = resp.data["token"]

    kudo_detail_url = reverse("kudo-detail", kwargs={"pk": kudo.pk})

    data = {"title": "Kudo Updated"}

    resp = client.patch(
        kudo_detail_url,
        data=data,
        HTTP_AUTHORIZATION=f"Token {token}",
        content_type="application/json",
    )
    assert resp.status_code == status.HTTP_200_OK


def test_create_kudo(client):
    organization = OrganizationFactory()
    user1 = UserFactory(password="qazwsxedc123!@#RFV", organization=organization)
    user2 = UserFactory(password="qazwsxedc123!@#RFV", organization=organization)

    kudo_data = model_to_dict(KudoFactory.build(by_user=user1, to_user=user2))

    token_generation_url = reverse("generate-token")

    credentials = {
        "username": user1.username,
        "password": "qazwsxedc123!@#RFV",
    }

    resp = client.post(token_generation_url, data=credentials)
    token = resp.data["token"]

    kudo_list_url = reverse("kudo-list")

    resp = client.post(
        kudo_list_url,
        data=kudo_data,
        HTTP_AUTHORIZATION=f"Token {token}",
        content_type="application/json",
    )

    assert resp.status_code == status.HTTP_201_CREATED


def test_create_kudo_same_user(client):
    organization = OrganizationFactory()
    user = UserFactory(password="qazwsxedc123!@#RFV", organization=organization)

    kudo_data = model_to_dict(KudoFactory.build(by_user=user, to_user=user))

    token_generation_url = reverse("generate-token")

    credentials = {
        "username": user.username,
        "password": "qazwsxedc123!@#RFV",
    }

    resp = client.post(token_generation_url, data=credentials)
    token = resp.data["token"]
    expected_data = {"detail": "You can not give kudo to yourself."}

    kudo_list_url = reverse("kudo-list")

    resp = client.post(
        kudo_list_url,
        data=kudo_data,
        HTTP_AUTHORIZATION=f"Token {token}",
        content_type="application/json",
    )

    assert resp.status_code == status.HTTP_403_FORBIDDEN
    assert resp.data == expected_data


def test_create_kudo_different_organization(client):
    organization1 = OrganizationFactory()
    organization2 = OrganizationFactory()
    user1 = UserFactory(password="qazwsxedc123!@#RFV", organization=organization1)
    user2 = UserFactory(password="qazwsxedc123!@#RFV", organization=organization2)

    kudo_data = model_to_dict(KudoFactory.build(by_user=user1, to_user=user2))

    token_generation_url = reverse("generate-token")

    credentials = {
        "username": user1.username,
        "password": "qazwsxedc123!@#RFV",
    }

    resp = client.post(token_generation_url, data=credentials)
    token = resp.data["token"]
    expected_data = {
        "detail": "You can not give kudo to someone who is not part your organization."
    }

    kudo_list_url = reverse("kudo-list")

    resp = client.post(
        kudo_list_url,
        data=kudo_data,
        HTTP_AUTHORIZATION=f"Token {token}",
        content_type="application/json",
    )

    assert resp.status_code == status.HTTP_403_FORBIDDEN
    assert resp.data == expected_data


def test_create_kudo_no_kudos_left(client):
    organization = OrganizationFactory()
    user1 = UserFactory(password="qazwsxedc123!@#RFV", organization=organization)
    user2 = UserFactory(password="qazwsxedc123!@#RFV", organization=organization)

    for hour in range(settings.KUDOS_MONTHLY_QUOTA):
        awarded = datetime.today().replace(
            day=1, hour=hour, minute=0, second=0, microsecond=0
        )
        KudoFactory(by_user=user1, to_user=user2, awarded=awarded)

    kudo_data = model_to_dict(KudoFactory.build(by_user=user1, to_user=user2))

    token_generation_url = reverse("generate-token")

    credentials = {
        "username": user1.username,
        "password": "qazwsxedc123!@#RFV",
    }

    resp = client.post(token_generation_url, data=credentials)
    token = resp.data["token"]
    expected_data = {"detail": "No kudos are available for the month."}

    kudo_list_url = reverse("kudo-list")

    resp = client.post(
        kudo_list_url,
        data=kudo_data,
        HTTP_AUTHORIZATION=f"Token {token}",
        content_type="application/json",
    )

    assert resp.status_code == status.HTTP_403_FORBIDDEN
    assert resp.data == expected_data


def test_kudos_endpoint_invalid_credential(client):
    organization = OrganizationFactory()
    user1 = UserFactory(password="qazwsxedc123!@#RFV", organization=organization)
    user2 = UserFactory(password="qazwsxedc123!@#RFV", organization=organization)
    KudoFactory.create_batch(15, by_user=user1, to_user=user2)
    KudoFactory.create_batch(15, by_user=user2, to_user=user1)
    kudo = KudoFactory(by_user=user2, to_user=user1)

    token = "some_invalid_token"
    expected_data = {"detail": "Invalid token."}

    kudo_list_url = reverse("kudo-list")
    resp = client.get(kudo_list_url, HTTP_AUTHORIZATION=f"Token {token}")
    assert resp.status_code == status.HTTP_401_UNAUTHORIZED
    assert resp.data == expected_data

    kudo_detail_url = reverse("kudo-detail", kwargs={"pk": kudo.pk})
    resp = client.get(kudo_detail_url, HTTP_AUTHORIZATION=f"Token {token}")
    assert resp.status_code == status.HTTP_401_UNAUTHORIZED
    assert resp.data == expected_data
