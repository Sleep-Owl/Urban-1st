grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]] # Список
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'} # Множество
students = list(students) # Конвертируем множество в список и сортируем по алфавиту
students.sort()
avg = sum(grades[0]) / len(grades[0]) # Считаем среднее по каждому списку
avg1 = sum(grades[1]) / len(grades[1])
avg2 = sum(grades[2]) / len(grades[2])
avg3 = sum(grades[3]) / len(grades[3])
avg4 = sum(grades[4]) / len(grades[4])
grades = [avg, avg1, avg2, avg3, avg4] # Объявляем новую переменную
studentsGrades = {students[0]:avg, students[1]:avg1, students[2]:avg2, students[3]:avg3, students[4]:avg4} # Объявляем словарь
print(studentsGrades)