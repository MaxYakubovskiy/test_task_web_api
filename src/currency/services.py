import requests
from config.settings import settings
from typing import Optional, List, Tuple
from currency.models import Currency, CurrencyRate


class CurrencyService:
    url = settings.API_URL

    @staticmethod
    def get_rates() -> Optional[List[dict]]:
        response = requests.get(CurrencyService.url, timeout=5)
        return response.json() if response.ok else None

    @staticmethod
    def parse_rates(data: list[dict]) -> list[tuple[str, float]]:
        mapping = {
            840: "USD",
            978: "EUR",
            826: "GBP",
            392: "JPY",
            756: "CHF",
            124: "CAD"
        }

        result = []

        for item in data:
            code = mapping.get(item.get("currencyCodeA"))
            if not code:
                continue

            rate = item.get("rateBuy") or item.get("rateCross")
            if item.get("currencyCodeB") != 980:
                continue

            if rate:
                result.append((code, rate))

        return result

    @staticmethod
    def save_rates(rates: List[Tuple[str, float]]) -> None:
        for code, rate in rates:
            currency, _ = Currency.objects.get_or_create(code=code)
            CurrencyRate.objects.create(currency=currency, rate=rate)

    @classmethod
    def update_rates(cls):
        data = cls.get_rates()
        rates = cls.parse_rates(data)
        if rates:
            cls.save_rates(rates)