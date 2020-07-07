# print("15.5".isdigit(), "15".isdigit())

try:
    a = {'one': 1, 'two': 2}
    # print({key + '1':value * 2 for key, value in a.items()})
    2 / 0
except ZeroDivisionError as r:
    print(r.args)
