from threading import Lock
from threading import Thread
import random
from time import sleep


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = Lock()

    
    def deposit(self):
        for i in range(100):
            random_chislo = random.randint(50,500)
            if random_chislo + self.balance < 500:
                self.lock.release
                self.balance += random_chislo
                print(f'Пополнение:{random_chislo},Баланс:{self.balance}')
            elif self.balance >= 500 and self.lock.locked():
                print("На балансе больше 500 рублей")
            sleep(0.001)
            
            
        

    def take(self):
        for i in range(100):
            random_chislo = random.randint(50,500)
            if random_chislo <= self.balance:
                self.balance -= random_chislo
                print(f'Снятие:{random_chislo},Баланс:{self.balance}')
            else:
                print(f'запрос на снятие {random_chislo}, баланс {self.balance}')
                print("Запрос отклонен, недостаточно средств")
            sleep(0.001)
            

bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
