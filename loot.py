import random
import time

s = time.time()
runs = 1000000
count = 0

for run in range(runs):
    if random.randint(1, 5) == 1:
        count += 1
    elif random.randint(1, 5) == 1:
        count += 1
    elif random.randint(1, 5) == 1:
        count += 1

print(count/runs)
print(time.time()-s)