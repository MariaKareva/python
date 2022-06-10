def sum_num():
    s = 0
    while True:
        err = False
        in_list = input("Enter numbers, input 'q' to exit: ").split()
        for num in in_list:
            if num.lower() == 'q':
                return s
            else:
                try:
                    s += int(num)
                except ValueError:
                    err = True
        if err:
            print("The data is not correct!")
            print(f"Sum of numbers = {s}")


print(sum_num())
