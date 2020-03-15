import pytest
from django.forms.models import model_to_dict
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token

from core.factories import OrganizationFactory, UserFactory

pytestmark = pytest.mark.django_db


def test_token_generation(client):
    user = model_to_dict(UserFactory(password="qazwsxedc123!@#RFV"))
    token = Token.objects.get(user=user["id"])

    token_generation_url = reverse("generate-token")

    credentials = {
        "username": user["username"],
        "password": "qazwsxedc123!@#RFV",
    }
    
    resp = client.post(token_generation_url, data=credentials)

    assert resp.status_code == status.HTTP_201_CREATED


def test_token_generation_invalid_credentials(client):
    user = model_to_dict(UserFactory(password="qazwsxedc123!@#RFV"))

    token_generation_url = reverse("generate-token")

    credentials = {
        "username": user["username"],
        "password": "some_wrong_password",
    }
    excepted_data = {
        "non_field_errors": ["Unable to log in with provided credentials."]
    }

    resp = client.post(token_generation_url, data=credentials)

    assert resp.status_code == status.HTTP_400_BAD_REQUEST
    assert resp.data == excepted_data


def test_token_deletion(client):
    user = model_to_dict(UserFactory(password="qazwsxedc123!@#RFV"))

    token_deletion_url = reverse("delete-token")
    token_generation_url = reverse("generate-token")

    credentials = {
        "username": user["username"],
        "password": "qazwsxedc123!@#RFV",
    }

    resp = client.post(token_generation_url, data=credentials)
    token = resp.data["token"]

    resp = client.get(token_deletion_url, HTTP_AUTHORIZATION=f"Token {token}")

    excepted_data = {"detail": "Authentication token deleted."}

    assert resp.status_code == status.HTTP_200_OK
    assert resp.data == excepted_data


def test_token_deletion_invalid_token(client):
    token = "some_invalid_token"
    token_deletion_url = reverse("delete-token")

    resp = client.get(token_deletion_url, HTTP_AUTHORIZATION=f"Token {token}")

    excepted_data = {"detail": "Invalid token."}

    assert resp.status_code == status.HTTP_401_UNAUTHORIZED
    assert resp.data == excepted_data


def test_token_deletion_no_token(client):
    token_deletion_url = reverse("delete-token")
    resp = client.get(token_deletion_url,)

    excepted_data = {"detail": "Authentication token was not provided."}

    assert resp.status_code == status.HTTP_400_BAD_REQUEST
    assert resp.data == excepted_data


def test_user_list(client):
    organization1 = OrganizationFactory()
    organization2 = OrganizationFactory()
    UserFactory.create_batch(5, organization=organization1)
    UserFactory.create_batch(5, organization=organization2)
    user = UserFactory(password="qazwsxedc123!@#RFV", organization=organization1)

    user = model_to_dict(user)

    token_generation_url = reverse("generate-token")

    credentials = {
        "username": user["username"],
        "password": "qazwsxedc123!@#RFV",
    }

    resp = client.post(token_generation_url, data=credentials)
    token = resp.data["token"]

    user_list_url = reverse("user-list")
    resp = client.get(user_list_url, HTTP_AUTHORIZATION=f"Token {token}")
    assert resp.status_code == status.HTTP_200_OK


def test_user_retrieve(client):
    organization = OrganizationFactory()
    user = UserFactory(password="qazwsxedc123!@#RFV", organization=organization)

    user = model_to_dict(user)

    token_generation_url = reverse("generate-token")

    credentials = {
        "username": user["username"],
        "password": "qazwsxedc123!@#RFV",
    }

    resp = client.post(token_generation_url, data=credentials)
    token = resp.data["token"]

    user_details_url = reverse("user-detail", kwargs={"username": user["username"]})
    resp = client.get(user_details_url, HTTP_AUTHORIZATION=f"Token {token}")
    assert resp.status_code == status.HTTP_200_OK


def test_user_retrieve_invalid_credential(client):
    user = model_to_dict(UserFactory(password="qazwsxedc123!@#RFV"))
    token = "some-invalid-token"

    excepted_data = {"detail": "Invalid token."}

    user_details_url = reverse("user-detail", kwargs={"username": user["username"]})
    resp = client.get(user_details_url, HTTP_AUTHORIZATION=f"Token {token}")

    assert resp.status_code == status.HTTP_401_UNAUTHORIZED
    assert resp.data == excepted_data


def test_user_partial_update(client):
    organization = OrganizationFactory()
    user = UserFactory(password="qazwsxedc123!@#RFV", organization=organization)

    user = model_to_dict(user)
    organization = model_to_dict(organization)

    token_generation_url = reverse("generate-token")

    credentials = {
        "username": user["username"],
        "password": "qazwsxedc123!@#RFV",
    }

    data = {"first_name": "fn", "last_name": "ln"}

    resp = client.post(token_generation_url, data=credentials)
    token = resp.data["token"]

    user_details_url = reverse("user-detail", kwargs={"username": user["username"]})
    resp = client.patch(
        user_details_url,
        data=data,
        HTTP_AUTHORIZATION=f"Token {token}",
        content_type="application/json",
    )

    assert resp.status_code == status.HTTP_200_OK


def test_user_partial_update_invalid_credential(client):
    user = model_to_dict(UserFactory(password="qazwsxedc123!@#RFV"))
    token = "some-invalid-token"

    excepted_data = {"detail": "Invalid token."}

    user_details_url = reverse("user-detail", kwargs={"username": user["username"]})
    resp = client.patch(
        user_details_url,
        data={"first_name": "i am root", "last_name": "the admin"},
        HTTP_AUTHORIZATION=f"Token {token}",
    )

    assert resp.status_code == status.HTTP_401_UNAUTHORIZED
    assert resp.data == excepted_data
