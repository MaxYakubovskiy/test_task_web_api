from rest_framework import serializers


class AddCurrencySerializer(serializers.Serializer):
    code = serializers.CharField(max_length=10)

class HistorySerializer(serializers.Serializer):
    code = serializers.CharField(max_length=3, required=True, help_text="Currency code, e.g., EUR")
    start_date = serializers.DateField(required=True, help_text="Start date in format YYYY-MM-DD")
    end_date = serializers.DateField(required=True, help_text="End date in format YYYY-MM-DD")