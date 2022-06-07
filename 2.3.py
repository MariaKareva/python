from typing import Dict, Any

month = int(input("Enter a month in numeric value from 1 to 12: "))

month_dict = {1: "jan", 2: "feb", 3: "mar", 4: "apr", 5: "may", 6: "jun", 7: "jul", 8: "aug", 9: "sep", 10: "oct", 11: "nov", 12: "dec"}

month_list = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]


if month in month_dict:
    print(f"{month}-th month of the year is {month_dict[month]}")
    print(f"{month}-th month of the year is {month_list[month - 1]}")
else:
    print("Wrong number!")

seasons_dict = {"winter": [12, 1, 2], "spring": [3, 4, 5], "summer": [6, 7, 8], "autumn": [9, 10, 11]}

month_num = int(input("Enter a numeric value of the month: "))

if month_num in sum(seasons_dict.values(), []):
    for i in seasons_dict.items():
        if month_num in i[1]:
            print(i[0])
            break
