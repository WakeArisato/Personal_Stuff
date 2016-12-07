import time 
import random
List_Range = input("What is the length of your list? ")
list = random.sample(range(int(List_Range)), int(List_Range))
def sorting(bad_list):
    M = int(0)
    length = len(bad_list) - 1
    Sorted = False
    while not Sorted:
        Sorted = True
        for i in range(length):
            if bad_list[i] > bad_list[i+1]:
                Sorted = False
                M = M + 1
                bad_list[i], bad_list[i+1] = bad_list[i+1], bad_list[i]
                print(list)
                time.sleep(.1)
    print(list)
    print(M)
sorting(list)

#Attempts
#1:2324
#2:2494
#3:2475
#4:2413
#5:2230
#6:2534
#avg = 2387.2