import sys
sys.path.append("C:\scripts")
sys.path.append(".\Defs")

print(sys.path)

from main import *
import definitions as defs

main_var = 'some string wind var'

if __name__ == '__main__':
    defs.functionTwo(main_var)
else:
    print(f'Execution module {__file__}')
