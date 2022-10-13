from payment import Payment
from datetime import date


class Boleto(Payment):
    def __init__(self, value, days_for_due_date=0) -> None:
        self._value = value
        self._days_for_due_date = date.today() + days_for_due_date

    def create_boleto_code(self):
        return f"{self._days_for_due_date}{self._value}"

    def pay(self):
        return True
