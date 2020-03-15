from rest_framework.serializers import ModelSerializer

from core.serializers import UserSerializer
from kudos.models import Kudo


class KudoListSerializer(ModelSerializer):
    class Meta:
        model = Kudo
        fields = ["id", "title", "description", "awarded"]
        read_only_fields = ["id"]


class KudoDetailSerializer(ModelSerializer):

    by_user = UserSerializer()
    to_user = UserSerializer()

    class Meta:
        model = Kudo
        fields = ["id", "title", "description", "by_user", "to_user", "awarded"]
        read_only_fields = ["id"]


class KudoCreateSerializer(ModelSerializer):
    def create(self, validated_data):

        kudo = Kudo.objects.create(
            by_user=self.context["request"].user, **validated_data
        )
        return kudo

    class Meta:
        model = Kudo
        fields = ["id", "title", "description", "to_user", "awarded"]
        read_only_fields = ["id"]
