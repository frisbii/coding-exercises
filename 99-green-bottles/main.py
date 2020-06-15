'''
Display the complete lyrics for the song: 
99 Bottles of Beer on the Wall.

The lyrics follow this form:

99 bottles of beer on the wall
99 bottles of beer
Take one down, pass it around
98 bottles of beer on the wall

98 bottles of beer on the wall
98 bottles of beer
Take one down, pass it around
97 bottles of beer on the wall

... and so on, until reaching 0.
'''

numbers = list(range(99, 0, -1))

plural = 's'
plural_2 = 's'

for i in numbers:
    if i == 1:
        plural = ''
        plural_2 = 's'
        amount_after = 'no'
    else:
        if i == 2:
            plural_2 = ''
        amount_after = i - 1
    print(f'''
    {i} green bottle{plural}, hanging on the wall
    {i} green bottle{plural}, hanging on the wall
    And if one green bottle should accidentally fall
    There'll be {amount_after} green bottle{plural_2}, hanging on the wall
    ''')