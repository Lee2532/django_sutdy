from rest_framework import serializers


class TestPostListSerializer(serializers.Serializer):
    a = serializers.CharField()
    b = serializers.CharField()
    c = serializers.CharField()
