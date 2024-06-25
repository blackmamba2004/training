# # 7-1
# car = input("What car would you take? ")
# print(f"Let me see if I can find you a {car.title()}!")
#
# # 7-2
# table_seats = int(input("На сколько человек вы хотите заказать стол? "))
# if table_seats > 8:
#     print("Вам придется подождать!")
# else:
#     print("Ваш стол готов!")
#
# # 7-3
# number = int(input("Введите число: "))
# if number % 10 == 0:
#     print(f"{number} кратно 10!")


# 7-5
price = 0
while True:
    age = input("Введите свой восзраст! ")
    if age == 'exit':
        break
    if int(age) < 3:
        price = 0
    elif 3 <= int(age) <= 12:
        price = 10
    elif int(age) > 12:
        price = 15
    print(f"Ваш билет стоит {price} $!")


sandwich_orders = ['с мясом', 'с колбасой', 'с сыром', 'с горчицей']
finished_sandwiches = []
i = 0
while i < len(sandwich_orders):
    order = sandwich_orders.pop(i)
    finished_sandwiches.append(order)
    print(f"Сэндвич {order} готов!")

print(finished_sandwiches)