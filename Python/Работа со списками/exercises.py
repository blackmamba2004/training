# 4-1
pizzas = ['pepperoni', 'mango', 'cheese']
for pizza in pizzas:
    print(f"I love this pizza: {pizza}!")

print("I think all pizzas!")

# 4-2
animals = ['dog', 'cat', 'fish']
for animal in animals:
    print(f"This {animal} is really great!")

print("I love all animals!")

# 4-3
for num in range(1, 21):
    print(num)

# 4-4
numbers = [num for num in range(1, 1_000_001)]
# for num in numbers:
#     print(num)

# 4-5

min_num = min(numbers)
max_num = max(numbers)
sum_nums = sum(numbers)
print(min_num, max_num, sum_nums)

# 4-6
odd_nums = []
for odd_num in range(1, 21, 2):
    odd_nums.append(odd_num)
    print(odd_num)

# 4-7
three_nums = [num for num in range(3, 31, 3)]
print(three_nums)

# 4-8
cub_nums = [num ** 3 for num in range(1, 11)]
print(cub_nums)

# 4-10

print(f"The first three items in the list are {numbers[:3]}")
print(f"Three items from middle of the list are {numbers[499_998:500_000]}")
print(f"The last three items in the list are: {numbers[-3:]}")
print(numbers[-1:-5:-1])

# 4-13

tuple_foods = ('apple', 'banana', 'pie', 'cucumber')
for food in tuple_foods:
    print(food)
