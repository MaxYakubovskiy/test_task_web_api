from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from ..models import Currency
from ..serializers import HistorySerializer


class CurrencyHistoryView(APIView):
    def get(self, request):
        serializer = HistorySerializer(data=request.query_params)
        if serializer.is_valid():
            code = serializer.validated_data["code"].upper()
            start = serializer.validated_data["start_date"]
            end = serializer.validated_data["end_date"]

            try:
                currency = Currency.objects.get(code=code)
                rates = currency.rates.filter(created_at__date__gte=start, created_at__date__lte=end)
                data = [{"rate": r.rate, "date": r.created_at} for r in rates]
                return Response({"code": code, "history": data}, status=status.HTTP_200_OK)
            except Currency.DoesNotExist:
                return Response({"detail": f"Currency {code} not found."}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
