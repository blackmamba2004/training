def greet_user(username):
    """
    Выводит простое приветствие
    """
    print(f"Hello, {username.title()}!")


greet_user('jesse')


def describe_pet(pet_name, animal_type='None_type'):
    print(animal_type)
    print(pet_name)


describe_pet(animal_type='elefant', pet_name='little jo')


describe_pet(pet_name='pitty')


def greet_users(names):
    for name in names:
        print(f"Привет, {name.title()}!")


usernames = ['jesse', 'pitty']
greet_users(usernames)