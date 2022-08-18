from payment import Payment


class Card(Payment):
    def __init__(self, number, holder, due_date, cvv) -> None:
        self._number = number
        self._holder = holder
        self._due_date = due_date
        self._cvv = cvv

    def get_holder(self):
        return self._holder

    def get_number(self):
        return self._number[-4:]

    def get_due_date(self):
        return self._due_date


class Debt(Card):
    def __init__(self, number, holder, due_date, cvv) -> None:
        super().__init__(number, holder, due_date, cvv)

    def pay(self):
        return True


class Credit(Card):
    def __init__(self, number, holder, due_date, cvv) -> None:
        super().__init__(number, holder, due_date, cvv)

    def pay(self):
        return True
