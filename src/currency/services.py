import requests
from dataclasses import dataclass
from src.config.settings import settings
from typing import Optional, List, Tuple
from currency.models import Currency, CurrencyRate


@dataclass
class CurrencyService:
    url: settings.API_URL

    @staticmethod
    def get_rates() -> Optional[List[dict]]:
        response = requests.get(CurrencyService.url, timeout=5)
        return response.json() if response.ok else None

    @staticmethod
    def parse_rates(data: List[dict]) -> List[Tuple[str, float]]:
        mapping = {
            840: "USD",
            978: "EUR"
        }

        result = []

        for i in data:
            code = mapping.get(i.get("currencyCodeA"))
            rate = i.get("rateBuy")
            if code and rate:
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