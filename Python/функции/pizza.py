# def make_pizza(*toppings):
#     print(toppings)
#
# make_pizza('pepperoni')
# make_pizza('mushrooms', 'extra cheese')


def make_pizza(title, size: int, *toppings):
    print(f"Мы делаем {title.title()} размером {size} со следующими добавками: ")
    for topping in toppings:
        print(f"- {topping}")

# make_pizza('peperoni', 16, 'cheese', 'mushrooms', 'extra cheese')