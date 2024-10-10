from threading import Thread
from time import sleep


class Knight(Thread):

    def __init__(self, name, power, enemies):
        super().__init__()
        self.name = name  
        self.power = power  
        self.enemies = enemies  
        self.days_fighting = 0  
    
    def run(self):
        print(f"{self.name}, на нас напали!")
        
        while self.enemies > 0:
            sleep(1) 
            self.days_fighting += 1
            
            self.enemies -= self.power
            if self.enemies < 0:
                self.enemies = 0
            
            print(f"{self.name}, сражается {self.days_fighting} день(дня)..., осталось {self.enemies} воинов.")

        print(f"{self.name} одержал победу спустя {self.days_fighting} дней(дня)!")

first_knight = Knight('Sir Lancelot', 10, 100)
second_knight = Knight("Sir Galahad", 20, 100)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print('Все битвы закончились')


