from rest_framework.serializers import ModelSerializer

from orders.models import SalesOrder


class OrderSerializer(ModelSerializer):
    class Meta:
        model = SalesOrder  #модель которую будем сериализовывать
        fields = ['amount', 'description']  # поля, которые будут взяты из модели