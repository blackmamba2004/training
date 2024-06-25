# 3-4
ghosts = ['Julia', 'Samuel', 'Peter', 'Tom']
print(f"Hello {ghosts[0]}! You and other {len(ghosts)-1} ghosts were added to this lobby")
print(f"Hello {ghosts[1]}! You and other {len(ghosts)-1} ghosts were added to this lobby")
print(f"Hello {ghosts[2]}! You and other {len(ghosts)-1} ghosts were added to this lobby")
print(f"Hello {ghosts[3]}! You and other {len(ghosts)-1} ghosts were added to this lobby")


# 3-5
print(f"Ghost {ghosts[0]} can't be added to this lobby")
ghosts[0] = 'Lois'
print(f"Hello {ghosts[0]}! You and other {len(ghosts)-1} ghosts were added to this lobby!")


# 3-6
print(f"The size of the lobby has been increased to 3 people!")
ghosts.insert(0, 'Klaudia')
ghosts.insert(len(ghosts) // 2, 'Frederik')
ghosts.append('Robert')
for ghost in ghosts:
    print(f"Hello {ghost}! You and other {len(ghosts)-1} ghosts were added to this lobby")
print(ghosts)


# 3-7
while len(ghosts) != 2:
    print(ghosts.pop())
print(ghosts)
del ghosts[1]
del ghosts[0]
print(ghosts)


# 3-8
countrys = ['USA', 'Japan', 'Russia', 'Spain', 'Germany']
print(countrys)
print(sorted(countrys))
print(countrys)
print(sorted(countrys, reverse=True))
print(countrys)
countrys.reverse()
print(countrys)
countrys.reverse()
print(countrys)
countrys.sort()
print(countrys)
countrys.sort(reverse=True)
print(countrys)