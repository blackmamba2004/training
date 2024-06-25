bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0])
bicycles[0] = 'yamaha'
print(bicycles[1].title())
print(bicycles[-1])
print(bicycles)

motorcycles = ['honda', 'yamaha', 'suzuki', 'honda']
motorcycles.append('ducati')
print(motorcycles)
motorcycles.insert(3, 'new_bike')
print(motorcycles)

del motorcycles[1]
print(motorcycles)
popped_bike = motorcycles.pop()
print(popped_bike)
print(motorcycles)
motorcycles.remove('honda')
print(motorcycles)

cars = ['audi', 'toyota', 'bmw', 'subaru']
cars.sort()
print(cars)

cars.sort(reverse=True)
print(cars)

new_cars = ['audi', 'toyota', 'lexus', 'ford', 'ferrari']
print(new_cars)
print(sorted(new_cars))
print(new_cars)
new_cars.reverse()
print(new_cars)
print(f'We sell now {len(new_cars)} cars')
