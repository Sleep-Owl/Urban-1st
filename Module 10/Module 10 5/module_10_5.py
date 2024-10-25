import multiprocessing
import time


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line)
    return all_data


# Создаем список названий файлов
file_names = [f'./Files/file {number}.txt' for number in range(1, 5)]

# # Вызываем функцию read_info для каждого файла линейно
# start_time = time.time()
# for name in file_names:
#     data = read_info(name)
# end_time = time.time()
# linear_execution_time = end_time - start_time
# print("Линейное выполнение:")
# print(linear_execution_time)

# Используем многопроцессный подход
if __name__ == '__main__':
    with multiprocessing.Pool(processes=6) as pool:
        start_time = time.time()
        pool.map(read_info, file_names)

    end_time = time.time()
    multiprocessing_execution_time = end_time - start_time
    print("Многопроцессное выполнение:")
    print(multiprocessing_execution_time)
