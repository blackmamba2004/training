# 6-1
bob = {'first_name': 'Bob', 'last_name': 'Kurtis', 'age': 20, 'city': 'New-York'}
print(bob)

# 6-2
favorite_numbers = {1: 'Bob', 2: 'Robert', 5: 'Daniel', 10: 'Max', 16: 'Sarah'}
print(favorite_numbers)

# 6-3
it_termins = {'dict': 'это структура, хранящая пары формата ключ-значение',
              'list': 'это список для хранения однотипных данных', 'tuple': 'это неизменяемый список'}
for key, value in it_termins.items():
    print(f"{key.title()} - {value}")

# 6-5
rivers_dict = {'nile': 'egypt', 'lena': 'russia', 'amazonka': 'brazil'}

for river, country in rivers_dict.items():
    print(f"River {river.title()} runs through {country.title()}.")

# 6-6
favorite_languages = {'bob': 'python', 'jen': 'ruby', 'edward': 'go', 'robert': 'c++', 'sarah': 'java'}
persons = ['bob', 'robert', 'martin', 'sarah', 'max', 'antony']

for person in persons:
    if person in favorite_languages.keys():
        print(f"{person.title()}, thank you for your pull!\n")
    else:
        print(f"{person.title()}, you don't have any favorite languages! :(\n")

# 6-7
person1 = {'first_name': 'john', 'last_name': 'doe', 'age': 20, 'city': 'New York'}
person2 = {'first_name': 'robert', 'last_name': 'frank', 'age': 25, 'city': 'Texas'}
person3 = {'first_name': 'james', 'last_name': 'smith', 'age': 23, 'city': 'Florida'}
persons = [person1, person2, person3]

for person in persons:
    print(person['first_name'].title(), person['last_name'], person['age'], person['city'])

# 6-10
favorite_numbers = {'Bob': [1, 25, 100], 'Robert': [2, 4],  'Daniel': [5, 50], 'Max': 10, 'Sarah': [16, 144]}
for person in favorite_numbers:
    print(person, favorite_numbers[person])

cities = {
    'amsterdam': {
        'country': 'Niderlands',
        'population': 2_000_000,
        'fact': 'много борделей!'
    },
    'new-york': {
        'country': 'USA',
        'population': 10_000_000,
        'fact': 'первый голландский город'
    }
}

for city, city_info in cities.items():
    print(city)
    for dd, tt in city_info.items():
        print(dd, tt)

