INSERT_AFTER_VALUE = "Hello"
STR_TO_INS = "my"
FILENAME = "myfile.txt"
with open(FILENAME, "w") as file :
    file.write("Hello file world!\n")
    #file.write("Hello file world2!\n")
"""
strings = []
with open(FILENAME, "r+") as file :
    strings_lst = file.readlines()
    for f in strings_lst :
        str_lst = f.split()
        idx = str_lst.index(INSERT_AFTER_VALUE)
        str_lst.insert(idx+1, STR_TO_INS)
        strings.append(" ".join(str_lst) + '\n')
    file.seek(0)
    file.writelines(strings)
    file.flush() # no sense
"""
with open(FILENAME, "r+") as file :
    #t = file.find(INSERT_AFTER_VALUE) + len(INSERT_AFTER_VALUE) + 1
    #f = f.replace(INSERT_AFTER_VALUE, INSERT_AFTER_VALUE + " " + STR_TO_INS)
    file.seek(6)
    file.write(" my")
    file.flush()
    #print(f)
    #break

