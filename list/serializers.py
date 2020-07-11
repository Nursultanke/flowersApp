from rest_framework import serializers


class FlowerSerializer(serializers.Serializer):
    owner_name = serializers.CharField(max_length=150)
    title = serializers.CharField(max_length=150)
    price = serializers.CharField(max_length=150)
    description = serializers.CharField()
    address = serializers.CharField(max_length=150)
    phone_number = serializers.CharField(max_length=150)
    image = serializers.ImageField()
