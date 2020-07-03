import datetime
filename = r"d:\PY\log.txt"
FILE_FOR_WRITE = r"d:\PY\Date_client.txt"
STR_FOR_COMPARE = '503 Unavailable'

with open(filename, 'r') as fl:
    lines_list = fl.readlines()

for line in lines_list:         # using slice
    str0 = line.split(',')[1]
    if str0[1:] == STR_FOR_COMPARE:
        print(line)

for line in lines_list:         # using trim string
    str0 = line.split(',')
    if str0[1].strip() == STR_FOR_COMPARE:
        print(line)
        date_client = str0
        date_client.pop(1)
        with open(FILE_FOR_WRITE, 'w') as fw:
            fw.write("".join(date_client))
            #print(str.join(date_client[0]))




