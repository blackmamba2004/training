first_name = 'ada'
last_name = 'lovelace'

name = first_name + ' ' + last_name
name_to_title = name.title()
name_to_lower = name.lower()
name_to_upper = name.upper()

print(name)
print(name_to_title)
print(name_to_lower)
print(name_to_upper)

print('Languages:\n\tPython\n\tC\n\tJava')
language = '    Python    '
print(language.rstrip(' '))
print(language.lstrip(' '))
print(language.strip(' '))

age = 20
message = 'Hello, ' + str(age) + ' years'
print(message)
