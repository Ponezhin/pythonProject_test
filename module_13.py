jun = 0
mid = 990
sen = 1390
print(f"Стоимость билетов на конференцию:\n Участники младше 18 лет - Бесплатно\n "
      f"Участники с 18 до 25 лет - {mid} руб.\n Участники с 25 лет - {sen} руб.\n "
      f"При приобретении 4-х и более билетов предоставляется скидка в размере 10% от суммы заказа.")
num_tickets = None
while True:
    try:
        num_tickets = int(input('Введите необходимое количество билетов:\n (Для выхода введите 0)\n'))
    except ValueError:
        num_tickets
        print("Введите необходимое количество билетов цифрами!")
    else:
        if num_tickets > 0:
            break
        else:
            break

discount = 10 if num_tickets >= 4 else 0
age_guests = {}
for i in range(num_tickets):
    while True:
        try:
            age = int(input(f'Введите возраст Участника {i + 1}:\n'))
            if 0 < age < 100:
                if age in age_guests.keys():
                    age_guests[age] += 1
                else:
                    age_guests[age] = 1
            else:
                print('Проверьте введенные данные!')
                continue
        except ValueError:
            print('Введите возраст участника цифрами!')
        else:
            break
print('')
print('Проверьте введенные данные:')
for key, value in age_guests.items():
    print(f'Возраст {key}, Количество {value}')
    if key < 18:
        age_guests[key] = jun * age_guests[key]
    elif 18 <= key < 25:
        age_guests[key] = mid * age_guests[key]
    else:
        age_guests[key] = sen * age_guests[key]

print('')
print(f'Сумма заказа:  {sum(age_guests.values())} руб.')
print(f'Размер скидки: {int(sum(age_guests.values()) * discount / 100)} руб.')
print(f'К оплате: {int(sum(age_guests.values())-(sum(age_guests.values()) * discount / 100))} руб.')