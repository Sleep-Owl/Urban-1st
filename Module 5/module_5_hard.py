import time
from datetime import datetime


class User:

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def password(self):
        return self.password

    def check_password(self, input_password):
        return self.password == hash(input_password)

    def get_age(self):
        return self.age

    def set_age(self, new_age):
        self.age = new_age

    def __str__(self):
        return f'{self.nickname}'


class Video:

    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def is_adult(self):
        return self.adult_mode

    def stop_at(self, stop_time):
        self.time_now += stop_time

    def elapsed_time(self):
        current_time = datetime.now()
        elapsed_seconds = (current_time - datetime(1970, 1, 1)).total_seconds()
        return elapsed_seconds

    def remaining_time(self):
        remaining_seconds = self.duration - self.time_now
        return remaining_seconds


class UrTube:

    def __init__(self):
        self.users = []  # список объектов User
        self.videos = []  # список объектов Video
        self.current_user = None  # текущий пользователь, объект User

    def log_in(self, nickname, password):
        for user in self.users:
            if user.nickname == nickname and user.password() == hash(password):
                self.current_user = user
                return True
        return False

    # метод register
    def register(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                print(f'Пользователь {nickname} уже существует')
                return False
        user = User(nickname, hash(password), age)
        self.users.append(user)
        self.current_user = user

    # метод log_out
    def log_out(self):
        self.current_user = None

    # метод add
    def add(self, *videos):
        for video in videos:
            if self.find_video(video.title) is None:
                self.videos.append(video)

    # поиск видео по названию
    def find_video(self, title):
        result = [video for video in self.videos if video.title == title]
        return result[0] if len(result) > 0 else None

    # получение списка названий видео, содержащих поисковое слово
    def get_videos(self, search_word):
        search_word = search_word.lower()
        result = []
        for video in self.videos:
            video_title = video.title.lower()
            if search_word in video_title:
                result.append(video_title)
        return list(set(result))

    # просмотр видео
    def watch_video(self, video_title):
        if self.current_user is not None:
            video = self.find_video(video_title)
            if video is not None and not video.adult_mode:
                self.time_now = 0
                while True:
                    time.sleep(1)
                    self.time_now += 1
                    print(self.time_now)
                    if self.time_now >= video.duration:
                        print("Конец видео")
                        break

            elif video is not None and video.adult_mode:
                if self.current_user.age < 18:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                else:
                    self.time_now = 0
                    while True:
                        time.sleep(1)
                        self.time_now += 1
                        print(self.time_now, end=' ')
                        if self.time_now >= video.duration:
                            print("Конец видео")
                            break

        else:
            print('Войдите в аккаунт, чтобы смотреть видео')


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
