my_list = [5, 6, 8, 9, 7, 5, 6, 6, 5, 7]
new_number = ""

while new_number != "q":
    i = 0
    new_number = input("Enter natural numbers in a row.\nTo exit = q\n")

    if new_number.isdigit():
        for n in my_list:
            if int(new_number) <= n:
                i += 1
            else:
                break
        my_list.insert(i, int(new_number))
    print(my_list)