per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input('Введите сумму:'))
bank1 = per_cent.get('ТКБ')
depbank1 = money*bank1/100
bank2 = per_cent.get('СКБ')
depbank2 = money*bank2/100
bank3 = per_cent.get('ВТБ')
depbank3 = money*bank3/100
bank4 = per_cent.get('СБЕР')
depbank4 = money*bank4/100
deposit = [depbank1, depbank2, depbank3, depbank4]
max_deposit = max(deposit)
print("Максимальная сумма, которую вы можете заработать:", max_deposit)
for item in deposit:
    print(item)