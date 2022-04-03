per_cent={'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
deposit=[]
money = input("Введите сумму депозита (рубли):")
money=int(money)
for key in per_cent:
    deposit.append(int(money*per_cent[key]/100))
print("Все возможные варианты:", deposit)
print("Максимальная сумма, которую вы можете заработать:", max(deposit))