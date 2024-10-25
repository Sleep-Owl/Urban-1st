import requests

url = 'https://urban-university.ru/profile/course?alias=course999421818026'

response = requests.get(url)

if response.status_code == 403:
    print("Запрос выполнен успешно!")
    print(response.text)  # Выводим ответ от сервера
else:
    print('Ошибка:', response.text)
