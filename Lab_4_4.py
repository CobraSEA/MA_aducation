'''
takes with input number of year
or range with ":" as separator like [year from]:[year to]
put "exit" for end program
print message of the year type (leapor not). If not then print closest leap year
if program get range of years, it print all leap years of the range
'''

try:
    year = ''
    while year != 'exit':
        year = input("Enter the year or range as [year from]:[year to] (or exit for end) :")
        if year == 'exit':
            break
        if year.find(':') >= 0: # find range and define list of years
            yf, yt = [int(q) for q in year.split(':')]
            lpy_lst = [str(i) for i in range(yf, yt + 1) if i % 4 == 0]
            lpy_lst = ", ".join(lpy_lst)
            print(f"Leap years are: {lpy_lst}")
        else:
            year = int(year)
            for y in range(year, year + 4):
                if y % 4 == 0:
                    if y % 100 != 0:
                        break
                    elif y % 400 == 0:
                        break
            if year == y:
                print(f"Year {y} is leap")
            else:
                print(f"Year {year} is not leap. Next leap year will be {y}")

except ValueError:
    print("Input value is not numeric.")
#else:
#    print("else way")
finally:
    print("game over")