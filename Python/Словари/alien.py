alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print(f"You just earned {new_points} points!")

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

alien_1 = dict(alien_0)
alien_1['speed'] = 'medium'

x_inc = 0

if alien_1['speed'] == 'slow':
    x_inc = 1
elif alien_1['speed'] == 'medium':
    x_inc = 2
else:
    x_inc = 3

alien_1['x_position'] = alien_1['x_position'] + x_inc
print(alien_1['x_position'], alien_1['y_position'])

del alien_1['color']


aliens = []
for i in range(30):
    aliens.append({'color': 'green', 'points': 5, 'speed': 'slow'})
print(len(aliens))

for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'

for alien in aliens[:5]:
    print(alien)