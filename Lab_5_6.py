FILENAME = r'C:\Users\cobra\PycharmProjects\MA_prog\MA_aducation\config.data'
lst = ['string1', 'string2', 'string3', 'string4', 'string5']

def writeConfig(file, string):
    if 'Configuration file! Do not modify!' in file.read():
        file.write(string)
    else:
        file.write(f'Configuration file! Do not modify! \n{string}')

def myDec(FILENAME, string):
    def writeConfigFile(FILENAME, string):
        with open(FILENAME, 'r+') as file:
            writeConfig(file, string)
    return writeConfigFile(FILENAME, string)

with open(FILENAME, 'w') as file:
    file.truncate()

for str_lst in lst:
    myDec(FILENAME,str_lst + '\n')


