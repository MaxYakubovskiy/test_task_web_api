from django.urls import path
from .views.current import CurrentRatesView
from .views.available import AvailableCurrenciesView
from .views.add import AddCurrencyView
from .views.history import CurrencyHistoryView
from .views.toggle import ToggleCurrencyView

urlpatterns = [
    path("rates/", CurrentRatesView.as_view(), name="current-rates"),
    path("available/", AvailableCurrenciesView.as_view(), name="available-currencies"),
    path("add/", AddCurrencyView.as_view(), name="add-currency"),
    path("history/", CurrencyHistoryView.as_view(), name="currency-history"),
    path("toggle/<str:code>/", ToggleCurrencyView.as_view(), name="toggle-currency"),
]