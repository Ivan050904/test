import hashlib
import time

class User:
    def __init__(self,nickname:str,password:str,age:int):
        self.nickname = nickname
        self.password = self._hash_password(password)
        self.age = age


    def _hash_password(self, password: str) -> int:
        hashed = hashlib.sha256(password.encode()).hexdigest()
        return int(hashed, 16) 
    
    def verify_password(self, password: str) -> bool:
        return self.password == self._hash_password(password)


class Video:
    def __init__(self,title:str,duration:int,adult_mode: bool = False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self,nickname,password):
        for user in self.users:
            if user.nickname == nickname and user.verify_password(password): 
                self.current_user = user
                print(f"Пользователь {nickname} успешно вошел в систему.")
                return
        print("Неправильный ник или пароль")


    def register(self,nickname,password,age):
        for user in self.users:
            if user.nickname == nickname:
                print(f'пользователь уже зарегестрирован')
                return

        new_user = User(nickname,password,age)
        self.users.append(new_user)
        self.current_user = new_user
        print(f'пользователь с ником {nickname} успешно зарегестрирован в системе')


    def log_out(self):
        self.current_user = None
        print("Вы вышли из аккаунта")
    

    def add(self, *videos):
        for video in videos:
            if any(existing_video.title == video.title for existing_video in self.videos):
                print(f"Видео с названием '{video.title}' уже существует")
                continue
            self.videos.append(video)
            print(f"Видео '{video.title}' успешно добавлено.")   
        

    def get_videos(self,stroka):
        result = []
        for video in self.videos:
            if stroka.lower() in video.title.lower():
                result.append(video.title)
        return result
    

    def watch_video(self, title):
        if self.current_user is None:
            print("Вы не вошли в аккаунт, пожалуйста войдите в аккаунт")
            return

        current_video = next((video for video in self.videos if video.title == title), None)


        if current_video is None:
            print("Видео не найдено")
            return

        if current_video.adult_mode and self.current_user.age < 18:
            print("Вам нет 18 лет, пожалуйста покиньте страницу")
            return

        print(f"Начинается воспроизведение видео: {current_video.title}")
        for second in range(current_video.time_now, current_video.duration):
            time.sleep(1)
            print(f"Секунда: {second + 1}")

        print("Конец видео")
        current_video.time_now = 0  


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
ur.log_out()
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')
ur.log_out()

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
