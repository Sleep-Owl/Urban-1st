from threading import Thread, Lock
import random
import time


class Bank:
    def __init__(self):
        super().__init__()
        self.balance = 0
        self.lock = Lock()

    def deposit(self):
        # self.lock.acquire()
        for i in range(100):
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
                time.sleep(0.001)
            else:
                rand = random.randint(50, 500)
                self.balance = self.balance + rand
                print(f'Пополнение: {rand}р. Баланс: {self.balance}р.')
                time.sleep(0.001)

    def take(self):
        for i in range(100):
            rand = random.randint(50, 500)
            print(f'Запрос на {rand}р.')
            if rand <= self.balance:
                self.balance = self.balance - rand
                print(f'Снятие: {rand}р. Баланс: {self.balance}р')
                time.sleep(0.001)
            else:
                print(f'Запрос отклонён, недостаточно средств')
                self.lock.acquire()
                time.sleep(0.001)


bk = Bank()

th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
