import datetime as dt

DATE_FORMAT = '%d.%m.%Y'


class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []
        self.spent = 0

    def add_record(self, record):
        self.records.append(record)

    def get_week_stats(self):
        today_date = dt.date.today()
        week_ago = today_date - dt.timedelta(days=7)
        return sum(
            day.amount for day in self.records
            if week_ago < day.date <= today_date
        )


class Record:
    def __init__(self, amount, comment, date=None):
        self.amount = amount
        self.comment = comment
        if date is None:
            self.date = dt.date.today()
        else:
            self.date = dt.datetime.strptime(date, DATE_FORMAT).date()

    def show(self):
        print(f"{self.amount}, {self.comment}, {self.date}.")


class CashCalculator(Calculator):

    def get_today_stats(self):
        spent = 0
        for i in self.records:
            if i.date == dt.date.today():
                spent += i.amount
        return f"Сегодня потрачено {spent} руб"

    def get_today_cash_remained(self, currency):
        spent = 0
        error = (f'Валюта "{currency}" не поддерживается')
        currencies = ['rub', 'eur', 'usd']
        if currency not in currencies:
            raise ValueError(error)
        for i in self.records:
            if i.date == dt.date.today():
                spent += i.amount
        if self.limit - spent > 0:
            if currency == 'rub':
                return f"На сегодня осталось {round((self.limit - spent), 2)} рублей"
            if currency == 'eur':
                return f"На сегодня осталось {round(((self.limit - spent) / 84), 2)} евро"
            if currency == 'usd':
                return f"На сегодня осталось {round(((self.limit - spent) / 74), 2)} долларов"

        if self.limit - spent == 0:
            return "Денег нет, держись"

        if self.limit - spent < 0:
            if currency == 'rub':
                return f"Денег нет, держись: твой долг {round((self.limit - spent), 2)} рублей"
            if currency == 'eur':
                return f"Денег нет, держись: твой долг {round(((self.limit - spent) / 84), 2)} евро"
            if currency == 'usd':
                return f"Денег нет, держись: твой долг {round(((self.limit - spent) / 74), 2)} долларов"


class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        got = 0
        for i in self.records:
            if i.date == dt.date.today():
                got += i.amount
        if self.limit - got > 0:
            return f"Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {self.limit - got} кКал"
        if self.limit - got <= 0:
            return "Хватит есть!"

    def get_today_stats(self):
        spent = 0
        for i in self.records:
            if i.date == dt.date.today():
                spent += i.amount
        return f"Сегодня съедено {spent} ККал"


if __name__ == "__main__":

    calories_calculator = CaloriesCalculator(2000)
    r4 = Record(amount=1200, comment="Кусок тортика. И ещё один.")
    r5 = Record(amount=84, comment="Йогурт")
    r6 = Record(amount=1140, comment="Баночка чипсов.", date="08.10.2020")

    calories_calculator.add_record(r4)
    calories_calculator.add_record(r5)
    calories_calculator.add_record(r6)

    print(calories_calculator.get_today_stats())

    print(calories_calculator.get_calories_remained())

    cash_calculator = CashCalculator(5000)

    r1 = Record(amount=145, comment="Безудержный шопинг", date="08.10.2020")
    r2 = Record(amount=5600, comment="Наполнение потребительской корзины")
    r3 = Record(amount=691, comment="Катание на такси", date="07.10.2020")

    cash_calculator.add_record(r1)
    cash_calculator.add_record(r2)
    cash_calculator.add_record(r3)

    print(cash_calculator.get_week_stats())

    print(cash_calculator.get_today_cash_remained("eur"))
