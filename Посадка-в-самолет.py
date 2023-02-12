def print_row(num_rows, chairs):
    for i in range(num_rows):
        for j in range(7):
            if chairs[i][j] == 0:
                print(".", end='')
            if chairs[i][j] == 1:
                print("#", end='')
            if chairs[i][j] == 2:
                print("_", end='')
        print()

def check(number, side, position, num_rows, chairs, free):
    for i in range(num_rows):
        if side == "left":
            if free[i][0] < number or (number == 2 and chairs[i][1] == 1) or (
                    position == "window" and chairs[i][0] == 1) \
                    or (position == "aisle" and chairs[i][2] == 1):
                continue
            if position == "window":
                if number == 1:
                    chairs[i][0] = 1
                    free[i][0] -= 1
                    print("Passengers can take seats: {}A".format(str(i + 1)))
                    return
                if number == 2:
                    chairs[i][0] = 1
                    chairs[i][1] = 1
                    free[i][0] -= 2
                    print("Passengers can take seats: {}A {}B".format(str(i + 1), str(i + 1)))
                    return
                if number == 3:
                    chairs[i][0] = 1
                    chairs[i][1] = 1
                    chairs[i][2] = 1
                    free[i][0] -= 3
                    print("Passengers can take seats: {}A {}B {}C".format(str(i + 1), str(i + 1), str(i + 1)))
                    return
            if position == "aisle":
                if number == 1:
                    chairs[i][2] = 1
                    free[i][0] -= 1
                    print("Passengers can take seats: {}C".format(str(i + 1)))
                    return
                if number == 2:
                    chairs[i][1] = 1
                    chairs[i][2] = 1
                    free[i][0] -= 2
                    print("Passengers can take seats: {}B {}C".format(str(i + 1), str(i + 1)))
                    return
                if number == 3:
                    chairs[i][0] = 1
                    chairs[i][1] = 1
                    chairs[i][2] = 1
                    free[i][0] -= 3
                    print("Passengers can take seats: {}A {}B {}C".format(str(i + 1), str(i + 1), str(i + 1)))
                    return
        else:
            if free[i][1] < number or (number == 2 and chairs[i][5] == 1) or (
                    position == "window" and chairs[i][6] == 1) \
                    or (position == "aisle" and chairs[i][4] == 1):
                continue
            if position == "window":
                if number == 1:
                    chairs[i][6] = 1
                    free[i][1] -= 1
                    print("Passengers can take seats: {}F".format(str(i + 1)))
                    return
                if number == 2:
                    chairs[i][6] = 1
                    chairs[i][5] = 1
                    free[i][1] -= 2
                    print("Passengers can take seats: {}E {}F".format(str(i + 1), str(i + 1)))
                    return
                if number == 3:
                    chairs[i][4] = 1
                    chairs[i][6] = 1
                    chairs[i][5] = 1
                    free[i][1] -= 3
                    print("Passengers can take seats: {}D {}E {}F".format(str(i + 1), str(i + 1), str(i + 1)))
                    return
            if position == "aisle":
                if number == 1:
                    chairs[i][4] = 1
                    free[i][1] -= 1
                    print("Passengers can take seats: {}D".format(str(i + 1)))
                    return
                if number == 2:
                    chairs[i][4] = 1
                    chairs[i][5] = 1
                    free[i][1] -= 2
                    print("Passengers can take seats: {}D {}E".format(str(i + 1), str(i + 1)))
                    return
                if number == 3:
                    chairs[i][4] = 1
                    chairs[i][6] = 1
                    chairs[i][5] = 1
                    free[i][1] -= 3
                    print("Passengers can take seats: {}D {}E {}F".format(str(i + 1), str(i + 1), str(i + 1)))
                    return
    print("Cannot fulfill passengers requirements")


if __name__ == "__main__":
    n = int(input())
    chairs = [[0] * 7] * n
    free = [[0] * 2] * n
    for i in range(n):
        l = input()
        num_left = 0
        num_right = 0
        for j in range(len(l)):
            if l[j] == '.':
                chairs[i][j] = 0
                if j <= 2:
                    num_left += 1
                else:
                    num_right += 1
            if l[j] == '#':
                chairs[i][j] = 1
            if l[j] == '_':
                chairs[i][j] = 2
        free[i][0] = num_left
        free[i][1] = num_right
    print_row(n, chairs)
    # num_group = int(input())
    # for i in range(num_group):
    #     s = list(input().split(" "))
    #     number = int(s[0])
    #     side = s[1]
    #     position = s[2]
    #     check(number, side, position, n, chairs, free)


