tumb = ['ножницы', 'карандаш', 'яблоко', 'книга']

for obj in tumb:
    print(obj)

it = iter(tumb)

try:
    while True:
        next_value = next(it)
        print(f"Текущее значение: {next_value}")

except StopIteration:
    print("Итерация окончена!")
