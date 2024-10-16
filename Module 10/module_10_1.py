import datetime
import time
import threading


def write_words(word_count, file_name):
  with open(file_name, 'w') as f:
    for i in range(1, word_count + 1):
      f.write(f'Какое-то слово № {i}\n')
      time.sleep(0.1)
  print(f"Завершилась запись в файл {file_name}")


time_start = datetime.datetime.now()

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

time_end = datetime.datetime.now()
print(f'Работа потоков: {time_end - time_start}')

time_start2 = datetime.datetime.now()

thr_first = threading.Thread(target=write_words, args=(10, 'example5.txt'))
thr_second = threading.Thread(target=write_words, args=(30, 'example6.txt'))
thr_third = threading.Thread(target=write_words, args=(200, 'example7.txt'))
thr_fourth = threading.Thread(target=write_words, args=(100, 'example8.txt'))

thr_first.start()
thr_second.start()
thr_third.start()
thr_fourth.start()

thr_first.join()
thr_second.join()
thr_third.join()
thr_fourth.join()
time_end2 = datetime.datetime.now()

print(f'Работа потоков: {time_end2 - time_start2}')
