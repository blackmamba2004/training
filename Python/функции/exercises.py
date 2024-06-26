# # 8-1
# def display_message():
#     print("Мы рассматриваем функции!")
#
#
# display_message()
#
#
# # 8-2
# def favorite_book(book):
#     print(f"My favorite book is {book.title()}!")
#
#
# favorite_book("ом уз")
#
#
# # 8-3
#
# # def make_shirt(size, text):
# #     print(f"Вы заказали майку размером {size} с текстом {text}")
# #
# # make_shirt('L', 'йохохо')
# # make_shirt(size='M', text='Fall Out Boy')
#
# # 8-4
#
# def make_shirt(size='L', text='I love Python!'):
#     print(f"Вы заказали майку размером {size} с текстом {text}")
#
#
# make_shirt()
#
#
# # 8-5
# def describe_sity(city, country='Russia'):
#     print(f"{city} - это город в {country}!")
#
#
# describe_sity('York')
# describe_sity('Moscow')
# describe_sity('Russia')
#
#
# # 8-6
# def city_country(city, country):
#     return f"{city.title()} - {country.title()}!"
#
#
# print(city_country('Moscow', 'Russia'))
#
#
# # 8-7
# def make_album(artist, title, audio_traks=''):
#     album = {'artist': artist.title(), 'title': title.title()}
#     if audio_traks:
#         album['audio_traks'] = audio_traks
#
#     return album
#
#
# album = make_album('metallica', 'black winter', 8)
# print(album)
#
#
# # 8-8
# while True:
#     print("Введите название артиста и полное имя")
#     artist = input("Артист: ")
#     if artist == 'quit':
#         break
#     title = input("Название: ")
#     if title == 'quit':
#         break
#     album = make_album(artist, title)
#     print(album)


# 8-9
def show_magicians(mag_names):
    for name in mag_names:
        print(name.title())


mag_names = ['bob', 'nelson', 'jack']
show_magicians(mag_names)


# 8-10
# при передаче списка в функцию, функция создает новый список, поэтому все изменения не затрагивают старый список.
# При использовании же среза [:] мы получаем доступ к элементам списка и можем их менять
def make_great(mag_names):
    mag_names[:] = [mag.title() + ' Great' for mag in mag_names]


make_great(mag_names)
show_magicians(mag_names)


# 8-12
def get_sandwich_components(sandwich, *additives):
    print(f"Это сэндвич {sandwich.title()}")
    for additive in additives:
        print(f" - добавка {additive.title()}")


get_sandwich_components('хот-дог', 'перец', 'кетчуп', 'майонез')


# 8-14
def make_car(model, manufacturer, **car_info):
    car = {
        'model': model,
        'manufacturer': manufacturer
    }
    for key, value in car_info.items():
        car[key] = value

    return car


car = make_car('BMW', 'Volkswagen', color='green', complectation='full')
print(car)