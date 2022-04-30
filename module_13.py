number_tickets = int(input("Введите количество билетов: "))
price_tickets = 0

for i in range(number_tickets):
    age = int(input("Введите возраст: "))
    i += 1
    if age < 18:
        print("Бесплатно!")
    elif 18 <= age <= 25:
        price_tickets += 990
        print("Цена билета 990 рублей")
    else:
        price_tickets += 1390
        print("Цена билета 1390 рублей")
if number_tickets > 3:
    price_tickets = price_tickets * 0.9
    print("Цена билетов с 10% скидкой для более 3 человек: ", price_tickets)
else:
    print("Общая сумма к оплате", price_tickets)
