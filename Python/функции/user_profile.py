def build_profile(first, last, **user_info):
    profile = {
        'first_name': first,
        'last_name': last
    }
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile('Symon', 'Vasiliev', city='Krasnodar', country='Russia', hobby='IT')
print(user_profile)