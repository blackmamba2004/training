magicians = ['alice', 'david', 'carolina']
for mag in magicians:
    print(f"Hello, {mag.title()}!\n")

print("Thank you everyone!")

for value in range(1, 11):
    print(f"His square is {value ** 2}")

numbers = list(range(1, 11, 2))
print(numbers)

squares = []
for sq in range(1, 11):
    squares.append(sq**2)
print(squares)

digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

min_digit = min(digits)
max_digit = max(digits)
sum_of_digits = sum(digits)
print(min_digit, max_digit, sum_of_digits, sep=', ')

inc_list = [value + 1 for value in range(2, 10)]
print(inc_list)