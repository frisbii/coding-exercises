'''
There are 100 doors in a row that are all initially closed.

You make 100 passes by the doors.

The first time through, visit every door and  toggle  the door  (if the door is closed,  open it;   if it is open,  close it).

The second time, only visit every 2nd door   (door #2, #4, #6, ...),   and toggle it.

The third time, visit every 3rd door   (door #3, #6, #9, ...), etc,   until you only visit the 100th door.
'''

for i in range(1,100):
    print('')

doors = {i:'Closed' for i in range(1,101)}

for i in range(1, 101):
    for j in range(0,101,i):
        if j != 0:
            doors[j] = 'Open' if doors[j] == 'Closed' else 'Closed'

for i in doors:
    print(f'Door {i}: {doors[i]}')
