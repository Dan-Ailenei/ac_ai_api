from rest_framework import serializers


class ResultSerializer(serializers.Serializer):
    # TODO: modify the length accordingly
    result = serializers.CharField(max_length=100)
