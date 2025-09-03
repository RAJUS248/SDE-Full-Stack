def get_Month_Str(month: int) -> str:
    match(month):
        case 1:
            return "Janauary"
        case 2:
            return "Feb"
        case 3:
            return "Mar"
        case 4:
            return "April"
        case 5:
            return "May"
        case 6:
            return "June"
        case 7:
            return "July"
        case 8:
            return "Aug"
        case 9:
            return "Sept"
        case 10:
            return "Oct"
        case 11:
            return "Nov"
        case 12:
            return "Dec"
        case _:
            return "Invalid month"

print(get_Month_Str(-1))
print(get_Month_Str(1))
print(get_Month_Str(5))
print(get_Month_Str(10))
print(get_Month_Str(15))

    