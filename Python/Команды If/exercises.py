food = 'banana'
if food == 'banana':
    print(food == 'banana')
    print("Yes, it's banana!")

car = 'Audi'
print(car.lower() == 'audi')

# 5-3
alien_color = 'red'
if alien_color == 'green':
    print("Вы заработали 5 очков!")

if alien_color == 'red':
    print("Вы заработали 5 очков!")

# 5-4
points = 0
if alien_color == 'green':
    points = 5
elif alien_color == 'yellow':
    points = 10
else:
    points = 15

print(f"Вы заработали {points} очков!")

fruits = ['apple', 'banana', 'mandarin', 'cherry']
if 'apple' in fruits:
    print("Yes, it's apple!")

if 'banana' in fruits:
    print("Yes, it's banana!")

# 5-8
users = ['Tom', 'John', 'Smith', 'Eric', 'admin']
users = []

if users:
    for user in users:
        if user == 'admin':
            print("Yes, it's admin!")
        else:
            print("No, it's")
else:
    print("We need new users!")

current_users = ['Tom', 'John', 'Sam', 'Rebeca', 'Robert']
new_users = ['Jerry', 'Sam', 'Bob', 'John', 'Jessica', 'JOHN']

for user in new_users:
    if user.title() in current_users:
        print("Вы не можете выбрать это имя!")
    else:
        print("Это имя доступно!")

string = 'medrocket'
if 'm' in 'medrocket':
    print("ok")