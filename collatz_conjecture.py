import sys

def step(n):
    if n % 2 == 0:
        return n/2
    else:
        return 3*n+1

while True:
    try:
        finished = False
        current_num = int(input())
        while finished != True:
            current_num = step(current_num)
            print(current_num)
            if int(current_num) == 1:
                finished = True
                print("\n")
    except ValueError:
        print("That's not a number. Try again!")
    except KeyboardInterrupt:
        sys.exit()
