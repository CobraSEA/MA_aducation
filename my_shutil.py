"""
Lab 6.8 module shutil
"""
import os
import shutil as sh

cur_folder = os.getcwd()

if 'folder_zip' in os.listdir():
    sh.rmtree('folder_zip')
if 'my_zip.zip' in os.listdir():
    os.remove('my_zip.zip')

os.mkdir('folder_zip')
for i in range(3):
    with open(os.path.join(cur_folder, 'folder_zip', f'file{i + 1}.data'), 'w') as file:
        file.write(f'some data of file {i + 1}')

sh.make_archive('my_zip', 'zip', root_dir='.', base_dir='./folder_zip')
sh.copy('my_zip.zip', os.path.join('..', 'my_zip.zip'))
sh.rmtree('folder_zip')
input('Press any key...')
sh.unpack_archive(os.path.join('..', 'my_zip.zip'), cur_folder, 'zip')
os.remove('my_zip.zip')
os.remove(os.path.join('..', 'my_zip.zip'))
print(sh.disk_usage(cur_folder))
