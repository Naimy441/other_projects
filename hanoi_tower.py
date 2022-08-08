'''
THE TOWER OF HANOI, made by Abdullah Naim.

The goal of the game of The Tower of Hanoi is to move the stack of disks
on one pole to another pole. There are three rules, however: (1) the player
can move only one disk at a time, (2) the player can only move disks to and
from the top of a tower, and (3) the player can never place a larger disk
on top of a smaller disk.

You can find more about the Tower of Hanio at https://en.wikipedia.org/wiki/Tower_of_Hanoi.
'''

def init_program(TOTAL_DISKS=5, DISK_BUILDING_BLOCK='#', DISK_RADIUS=2, EMPTY_POLE_LAYER='|||'):
    # Creates the look of the disks that will be used in the game, depending on TOTAL_DISKS
    DISKS = {}
    for i in range(1, TOTAL_DISKS + 1):
        # (i+1)*DISK_RADIUS is length of the disk, excluding the number in the middle
        DISKS[i] = str(i).center((i + 1)*DISK_RADIUS + 1, DISK_BUILDING_BLOCK)


    poles = {
        'A' : [],
        'B' : [],
        'C' : []
    }

    # Adds the desired number of pole layers to each pole, depending on TOTAL_DISKS
    for pole in poles.values():
        for i in range(TOTAL_DISKS + 1):
            pole.append(EMPTY_POLE_LAYER)

    # Then adds TOTAL_DISKS number of disks to the first pole, starting at the second layer
    for i in range(1, TOTAL_DISKS + 1):
        poles['A'][i] = DISKS[i]
