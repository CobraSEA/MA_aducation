import os
#import sys

#for k, v in os.environ.items():
#    print(k, v)

print(os.environ['COMPUTERNAME'], os.environ['PROCESSOR_ARCHITEW6432'])
wrkdir = os.getcwd()
print(wrkdir)
os.chdir('C:/')
print(os.getcwd())
# for ls in os.listdir(path='.'):
#    print(ls)

flist = {}
for line in os.listdir('.'):
    if os.path.isdir(line):
        flist.update({line: 'dir'})
    else:
        if os.path.islink(line):
            flist.update({line: 'link'})
        else:
            flist.update({line: 'file'})

print(', '.join([file for file, ttype in flist.items() if ttype == 'dir']))
print(', '.join([file for file, ttype in flist.items() if ttype == 'file']))
print(', '.join([file for file, ttype in flist.items() if ttype == 'link']))

# file_list = [ls for ls in os.listdir('.') if os.path.isfile(ls)]
# link_list = [ls for ls in os.listdir('.') if os.path.islink(ls)]

os.chdir(wrkdir)
os.mkdir('Temp')
print([name for name in os.listdir(wrkdir) if name == 'Temp'])
os.rmdir('Temp')

os.path