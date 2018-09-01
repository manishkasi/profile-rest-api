from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """Serializes a name field to test our API view."""

    name = serializers.CharField(max_length=10)
