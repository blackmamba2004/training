cars = ['audi', 'bmw', 'subaru', 'toyota']
new_cars = tuple([car.upper() if car == 'bmw'
                  else car.title() if car == 'audi'
                  else car.lower() for car in cars[:]])
print(new_cars)
cars.remove('bmw')
print(new_cars)
