#!/usr/bin/python3
for i in range(10):

    for j in range(10):
        if i >= j:
            continue

        print(f"{i}", end="")
    
        if (i == 8) and (j == 9):
            print(f"{j}")
        else:
            print(f"{j}", end=", ")
