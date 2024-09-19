import os
import time

print(os.getcwd())
print(os.path.join(r'D:\Disc D\Program Files\PyCharm Community Edition 2024.1.4\My projects\Urban-1st\Module 7',
                   'module_7_5.py'))
print(os.path.getmtime(
    r'D:\Disc D\Program Files\PyCharm Community Edition 2024.1.4\My projects\Urban-1st\Module 7\module_7_5.py'))
modified_time = os.path.getmtime(
    r'D:\Disc D\Program Files\PyCharm Community Edition 2024.1.4\My projects\Urban-1st\Module 7\module_7_5.py')
c_time = time.ctime(modified_time)
print(c_time)
print(os.path.getsize(
    r'D:\Disc D\Program Files\PyCharm Community Edition 2024.1.4\My projects\Urban-1st\Module 7\module_7_5.py'))
path = r'D:\Disc D\Program Files\PyCharm Community Edition 2024.1.4\My projects\Urban-1st\Module 7\module_7_5.py'
dirname = os.path.dirname(path)
print(dirname)

for root, dirs, files in os.walk(
        r'D:\Disc D\Program Files\PyCharm Community Edition 2024.1.4\My projects\Urban-1st\Module 7'):
    for file in files:
        filepath = r'D:\Disc D\Program Files\PyCharm Community Edition 2024.1.4\My projects\Urban-1st\Module 7'
        filetime = 1726747972.9122403
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = 1281
        parent_dir = r'D:\Disc D\Program Files\PyCharm Community Edition 2024.1.4\My projects\Urban-1st\Module 7'
        print(
            f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')
