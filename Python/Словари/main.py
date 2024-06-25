str_input = 'medrocketmedrocketmedrocket'
word = 'medrocket'

word_dict = {letter: word.count(letter) for letter in set(word)}

str_input_dict = {letter: str_input.count(letter) // value
                  for letter, (key, value) in zip(set(word), word_dict.items())}

min_el = min(str_input_dict.values())

print(min_el)
