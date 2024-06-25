favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}
print(favorite_languages['sarah'].title())

for name in favorite_languages.keys():
    print(name.title())

print("\n")
for name in sorted(favorite_languages.keys()):
    print(name)

for language in favorite_languages.values():
    print(language.title())