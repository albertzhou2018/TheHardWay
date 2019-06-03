
def while_test(loop_time):
    # i = 0
    # numbers = []
    #
    #
    # while i < loop_time:
    #     print(f"At the top i is {i}")
    #     numbers.append(i)
    #
    #     i = i + increment
    #     print("Numbers now: ", numbers)
    #     print(f"At the bottom i is {i}")
    #
    # print("The numbers: ")
    #
    # for num in numbers:
    #     print(num)


    # for-loop
    numbers = []

    for i in range(0, loop_time):
        print(f"At the top i is {i}")
        numbers.append(i)

        print("Number now: ", numbers)
        print(f"At the bottom i is {i}")
    print("The numbers: ")

    for num in numbers:
        print(num)
