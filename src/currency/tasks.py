from celery import shared_task
from .services import CurrencyService


@shared_task(bind=True, autoretry_for=(Exception,), retry_backoff=1, max_retries=5)
def update_rates(self):
    data = CurrencyService.get_rates()
    rates = CurrencyService.parse_rates(data)
    CurrencyService.save_rates(rates)