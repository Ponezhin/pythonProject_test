per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input("Введите сумму вклада в рублях:"))
b1 = per_cent.get('ТКБ')
b2 = per_cent.get('СКБ')
b3 = per_cent.get('ВТБ')
b4 = per_cent.get('СБЕР')
bank1 = round(b1 / 100 * money)
bank2 = round(b2 / 100 * money)
bank3 = round(b3 / 100 * money)
bank4 = round(b4 / 100 * money)

deposit = [bank1, bank2, bank3, bank4]
print("Money =", money, "руб.")
print("Bank =", (', '.join(per_cent.keys())))
print("Deposit =", deposit)
print("Максимальная сумма, которую вы можете заработать —", max(deposit), "руб.")