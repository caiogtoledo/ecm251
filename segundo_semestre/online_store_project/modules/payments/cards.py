from payment import Payment


class Card(Payment):
    def __init__(self, number, holder, due_date) -> None:
        self._number = number
        self._holder = holder
        self._due_date = due_date

    def get_holder(self):
        return self._holder

    def get_number(self):
        return self._number[-4:]

    def get_due_date(self):
        return self._due_date
