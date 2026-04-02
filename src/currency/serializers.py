from rest_framework import serializers


class AddCurrencySerializer(serializers.Serializer):
    code = serializers.CharField(max_length=10)

class HistorySerializer(serializers.Serializer):
    code = serializers.CharField(max_length=10)
    start_date = serializers.DateField()
    end_date = serializers.DateField()