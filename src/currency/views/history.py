from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from ..models import Currency
from ..serializers import HistorySerializer


class CurrencyHistoryView(APIView):
    def get(self, request):
        serializer = HistorySerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)

        code = serializer.validated_data["code"].upper()
        start_date = serializer.validated_data["start_date"]
        end_date = serializer.validated_data["end_date"]

        rates = Currency.objects.filter(
            currency_code=code,
            date__date__gte=start_date,
            date__date__lte=end_date
        ).order_by("date")

        data = [
            {"date": r.date, "rate": r.rate} for r in rates
        ]
        return Response(data, status=status.HTTP_200_OK)