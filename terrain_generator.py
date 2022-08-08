'''
Terrain Generator - Abdullah Naim
'''

import random
import keyboard
import time

RENDER_DISTANCE = 3

def return_new_chunk_data():
    return random.randint(0, 10)

def return_new_terrain(render_distance):
    terrain = [[None for i in range(RENDER_DISTANCE)] for i in range(RENDER_DISTANCE)]
    for x in range(render_distance):
        for y in range(render_distance):
            terrain[x][y] = return_new_chunk_data()
    return terrain

def update_terrain(event):
    if event.name == 'right':
        pass
    elif event.name == 'left':
        pass
    elif event.name == 'up':
        pass
    elif event.name == 'down':
        pass

terrain = return_new_terrain(RENDER_DISTANCE)
rendered_terrain = terrain

keyboard.on_release(update_terrain)

while True:
    print(rendered_terrain)
    time.sleep(2.5)
