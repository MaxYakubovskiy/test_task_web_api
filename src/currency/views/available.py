from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from src.currency.models import Currency



class AvailableCurrenciesView(APIView):
    ALL_CURRENCIES = ["USD", "EUR", "GBP", "JPY", "CHF", "CAD"]

    def get(self, request):
        try:
            existing = Currency.objects.values_list("code", flat=True)
            available = [c for c in self.ALL_CURRENCIES if c not in existing]
            return Response({"available_currencies": available}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


