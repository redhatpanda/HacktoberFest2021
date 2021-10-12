import tkinter
import  datetime
import  requests

class CurrencyConverter :
    def __init__(self,from_currency,to_currency,from_currency_value):
        self.datenow = datetime.date.today()
        self.from_currency_value = from_currency_value
        self.money = 0
        self.from_currency = from_currency
        self.to_currency = to_currency
        self.parameter = {
            "from_currency": f"{self.from_currency}",
            "to_currency": f"{self.to_currency}",
            "apikey": "WMRXZH90EW47HY6S",

        }
        self.converted = requests.get(url="https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE",
                                 params=self.parameter)
        # print(self.converted.json())
        # self.from_currency = from_currency
        # self.to_currency = to_currency
        # self.from_currency_value = from_currency_value
        # self.to_currency_value = to_currency_value


    def converter(self):
        self.money = float(self.from_currency_value) * float(self.converted.json()['Realtime Currency Exchange Rate']['5. Exchange Rate'])
        return round(self.money,2)


    def title(self):

        return f" 1 {self.from_currency} = {self.converted.json()['Realtime Currency Exchange Rate']['5. Exchange Rate']} {self.converted.json()['Realtime Currency Exchange Rate']['4. To_Currency Name']} \n {self.datenow.strftime('%d/%m/%Y')}"



