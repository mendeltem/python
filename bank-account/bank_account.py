from threading import RLock

class BankAccount(object):
    def __init__(self):
        self.money = 0
        self.active = 0
        self._lock = RLock();

    def get_balance(self):
        if self.active:
            return self.money
        else:
            raise ValueError("Account not active")

    def open(self):
        if self.active ==0:
            self.active = 1

    def deposit(self, amount):
        with self._lock:
            if self.active and amount >0:
                self.money += amount
            else:
                raise ValueError("Account not active")

    def withdraw(self, amount):
        with self._lock:
            if self.active and  0 < amount <= self.money:
                self.money -= amount
            else:
                raise ValueError("Account not active")

    def close(self):
        if self.active:
            self.active = 0

