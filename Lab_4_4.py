try:
    year = 1
    while year != 0:
        year = input("Enter the year or 0 for exit or range as [year from]:[year to]:")
        if year == '0':
            break
        if year.find(':') != 0: # find range and define list of years
            rng = year.split(':')
            lpy_lst = [str(i) for i in range(int(rng[0]), int(rng[1]) + 1) if i % 4 == 0]
            lpy_lst = ", ".join(lpy_lst)
            print(f"Leap years are: {lpy_lst}")
        else:
            laep = int(year)
            leap = year % 4
            if leap == 0:
                print(f"Year {year} is leap")
            else:
                print(f"Year {year} is not leap. Next leap year will be {year + leap}")

except ZeroDivisionError:
    print("Input value is not numeric.")
#else:
#    print("else way")
finally:
    print("game over")