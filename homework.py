import datetime as dt


class Calculator:
    def __init__(self, balance):
        self.balance = balance
        self.records = []
        self.spent = 0

    def add_record(self, record):
        self.records.append(record)
        if record.date == (dt.datetime.now()).date():
            self.balance -= record.amount

    def get_week_stats(self):
        current_week = []
        week_amount = 0
        for i in range(7):
            current_week.append(dt.datetime.now() - dt.timedelta(days=i))
        for i in self.records:
            if i.date in current_week:
                week_amount += i.amount
        return week_amount


class Record:
    def __init__(self, amount, comment, date=None):
        if date is None:
            date = (dt.datetime.now()).date()
        self.amount = amount
        self.comment = comment
        self.date = date


class CashCalculator(Calculator):

    def get_today_stats(self):
        spent = 0
        for i in self.records:
            if i.date == (dt.datetime.now()).date():
                spent += i.amount
        return f"Сегодня потрачено {spent} руб"

    def get_today_cash_remained(self, currency):
        if self.balance > 0:
            if currency == 'rub':
                return f"На сегодня осталось {self.balance} рублей"
            if currency == 'eur':
                return f"На сегодня осталось {self.balance / 84} евро"
            if currency == 'usd':
                return f"На сегодня осталось {self.balance / 74} долларов"

        if self.balance == 0:
            return "Денег нет, держись"

        if self.balance < 0:
            if currency == 'rub':
                return f"Денег нет, держись: твой долг {self.balance} рублей"
            if currency == 'eur':
                return f"Денег нет, держись: твой долг {self.balance / 84} евро"
            if currency == 'usd':
                return f"Денег нет, держись: твой долг {self.balance / 74} долларов"


class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        if self.balance > 0:
            return f"Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {self.balance} кКал"
        if self.balance <= 0:
            return "Хватит есть!"

    def get_today_stats(self):
        spent = 0
        for i in self.records:
            if i.date == (dt.datetime.now()).date():
                spent += i.amount
        return f"Сегодня съедено {spent} ККал"


cash_calculator = CashCalculator(1000)
cash_calculator.add_record(Record(amount=145, comment="кофе"))
cash_calculator.add_record(Record(amount=300, comment="Серёге за обед"))
cash_calculator.add_record(Record(amount=3000, comment="бар в Танин др", date="08.11.2019"))
print(cash_calculator.get_today_cash_remained("rub"))
