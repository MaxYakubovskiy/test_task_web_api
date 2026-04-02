from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from src.currency.models import Currency



class CurrentRatesView(APIView):
    def get(self, request):
        currencies = Currency.objects.filter(is_active=True).prefetch_related("rates")
        result = []
        for currency in currencies:
            last_rate = currency.rates.first()
            result.append({"code": currency.code, "rate": last_rate.rate if last_rate else None})
        return Response(result, status=status.HTTP_200_OK)