from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from src.currency.models import Currency
from src.currency.serializers import AddCurrencySerializer


class AddCurrencyView(APIView):
    def post(self, request):
        serializer = AddCurrencySerializer(data=request.data)
        if serializer.is_valid():
            code = serializer.validated_data["code"].upper()
            currency, created = Currency.objects.get_or_create(code=code)
            if created:
                return Response({"detail": f"Currency {code} added."}, status=status.HTTP_201_CREATED)
            else:
                return Response({"detail": f"Currency {code} already exists."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
