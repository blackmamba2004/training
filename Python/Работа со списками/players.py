players = ['rebecca', 'junior', 'dan', 'charles', 'johny']
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:])
print(players[-3:])

for player in players[0:3]:
    print(player)

my_foods = ['banana', 'apple', 'pie']
friend_foods = my_foods[:]
my_foods.remove('apple')
print(friend_foods)