class Accounts:
    def __init__(self, id=0, balance=0):
        self.__id = id
        self.__balance = balance

    def setId(self, id):
        self.__id = id

    def getId(self):
        return self.__id

    def setBalance(self, balance):
        self.__balance += balance

    def getBalance(self):
        return format(self.__balance, ".2f")

    def withdrawal(self, withdrawalAmount):
        if withdrawalAmount < self.__balance:
            self.__balance -= withdrawalAmount
        else:
            print("Insufficient Funds")
