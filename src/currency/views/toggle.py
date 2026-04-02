from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from src.currency.models import Currency



class ToggleCurrencyView(APIView):
    def post(self, request, code: str):
        code = code.upper()
        try:
            currency = Currency.objects.get(code=code)
            currency.is_active = not currency.is_active
            currency.save()
            status_str = "on" if currency.is_active else "off"
            return Response({"detail": f"Monitoring currency {code} {status_str}."}, status=status.HTTP_200_OK)
        except Currency.DoesNotExist:
            return Response({"detail": f"Currency {code} not found."}, status=status.HTTP_404_NOT_FOUND)