def main(num_doors:int):
    num_doors += 1
    
    doors = [False] * num_doors

    for i in range(1, num_doors):
        for j in range(i, num_doors, i):
            doors[j] = not doors[j]

    for i in range(num_doors):
        if doors[i]:
            print(i, ": ", doors[i])


if __name__ == "__main__":
    main(100)
