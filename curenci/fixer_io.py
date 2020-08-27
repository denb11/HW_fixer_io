import json
from os import path
import requests
import datetime

today = datetime.datetime.now()
ymd = (str(today)).split(' ')[0]
file_name = f'rates--{ymd}.json'
print((str(today)).split(' ')[0])

key = '664db39a8f01d144d3bda05cbcde2278'
endpoint = 'http://data.fixer.io/api/latest' + '?access_key=' + key


def files():
    global eur, mdl, usd, rub
    if path.exists(file_name):
        file = open(file_name, 'r')
        data = json.loads(file.read())
    else:
        response = requests.get(endpoint)
        data = json.loads(response.text)

        file = open(file_name, 'w')
        file.write(response.text)
        file.close()

    if data['success'] is False:
        print("CANNOT ACCESS DATA")
    else:
        eur = 1.0
        mdl = data['rates']['MDL']
        usd = data['rates']['USD']
        rub = data['rates']['RUB']
    print(f">>> Pretul pt un euro: {mdl:10.4f} MDL {usd:10.4f} USD {rub:10.4f} RUB")
    print("-" * 80)

    def convert():
        if val == "EUR":
            if val2 == "USD":
                exit_m = money1 * usd
                print(exit_m, "USD")
            elif val2 == "RUB":
                exit_m = money1 * rub
                print(exit_m, "RUB")
            elif val2 == "MDL":
                exit_m = money1 * mdl
                print(exit_m, "MDL")
            elif val2 == "EUR":
                print(money1, "EUR")
            else:
                print("Valuta gresita1")

        elif val == "USD":
            if val2 == "EUR":
                exit_m = money1 / usd
                print(exit_m, "EUR")
            elif val2 == "RUB":
                exit_m = money1 / usd * rub
                print(exit_m, "RUB")
            elif val2 == "MDL":
                exit_m = money1 / usd * mdl
                print(exit_m, "MDL")
            elif val2 == "USD":
                print(money1, "USD")
            else:
                print("Valuta gresita")

        elif val == "RUB":
            if val2 == "EUR":
                exit_m = money1 / rub
                print(exit_m, "EUR")
            elif val2 == "USD":
                exit_m = money1 / rub * usd
                print(exit_m, "USD")
            elif val2 == "MDL":
                exit_m = money1 / rub * mdl
                print(exit_m, "MDL")
            elif val2 == "RUB":
                print(money1, "RUB")
            else:
                print("Valuta gresita")

        elif val == "MDL":
            if val2 == "EUR":
                exit_m = money1 / mdl
                print(exit_m, "EUR")
            elif val2 == "USD":
                exit_m = money1 / mdl * usd
                print(exit_m, "USD")
            elif val2 == "RUB":
                exit_m = money1 / mdl * rub
                print(exit_m, "RUB")
            elif val2 == "MDL":
                print(money1, "MDL")
            else:
                print("Valuta gresita")
        else:
            print("eroare")

    money1 = float(input(f'Introduceti suma:'))
    val    = str(input("Inrtoduceti valuta: "))
    val2   = str(input("Introduceti valuta finala: "))
    convert()

def menu():
    option = -1
    while option != 0:
        print("########## MENU ###########")
        print("###########################")
        print("1. Start convert")
        print("2. Finis")
        option = int(input())

        if option == 1:
            files()

        if option == 2:
            break

menu()
