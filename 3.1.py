def div(s_1, s_2):
    try:
        s_1, s_2 =int(s_1), int(s_2)
        div_num = s_1 / s_2
    except ValueError:
        return "Value Error"
    except ZeroDivisionError:
        return "Division by zero is a ban!"
    return round(div_num, 4)


print(div(input("Enter the first number: "), input("Enter the second number: ")))