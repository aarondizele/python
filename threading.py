import threading
import time
import random


# def executeThread(n):
#     print("Thread {} sleeps at {}\n".format(n,time.strftime("%H:%M:%S",time.gmtime())))

#     randSleepTime = random.randint(1,5)

#     time.sleep(randSleepTime)
#     print("Thread {} stops sleeping at {}\n".format(n, time.strftime("%H:%M:%S", time.gmtime())))


# for i in range(10):
#     thread = threading.Thread(target=executeThread, args=(i,))
#     thread.start()

#     print("Active Threads: ", threading.activeCount())
#     # print("Thread Objects: ", threading.enumerate())

# class CustThread(threading.Thread):
#     def __init__(self, name):
#         threading.Thread.__init__(self)
#         self.name = name
#
#     def run(self):
#         getTime(self.name)
#         print("Thread", self.name, "Execution End")
#
#
# def getTime(name):
#     print("Thread {} sleeps at {}".format(name, time.strftime("%H:%M:%S", time.gmtime())))
#
#     randSleepTime_ = random.randint(1, 5)
#     time.sleep(randSleepTime_)
#
#
# thread1 = CustThread("1")
# thread2 = CustThread("2")
#
# thread1.start()
# thread2.start()
#
# print("Thread 1 alive :", thread1.is_alive())
# print("Thread 2 alive :", thread2.is_alive())
#
# print("Thread 1 name :", thread1.getName())
#
# print("Thread 2 name :", thread1.getName())




class BankAccount(threading.Thread):

    acctBalance = 100

    def __init__(self, name, moneyRequest):
        threading.Thread.__init__(self)
        self.name = name
        self.moneyRequest = moneyRequest

    def run(self):
        threadLock.acquire() ### lock thread
        BankAccount.getMoney(self)
        threadLock.release() ### delock thread after                                calling getMoney

    @staticmethod
    def getMoney(customer):
        print("{} tries to withdrawal ${} at {}".format(customer.name, customer.moneyRequest, time.strftime("%H:%M:%S", time.gmtime())))
        if BankAccount.acctBalance - customer.moneyRequest > 0:
            BankAccount.acctBalance -= customer.moneyRequest
            print("New account balance: ${}".format(BankAccount.acctBalance))
        else:
            print("Not enough money in your account")
            print("Current balance: ${}".format(customer.acctBalance))
        time.sleep(3)

threadLock = threading.Lock()
doug = BankAccount("Doug", 20)
paul = BankAccount("Paul", 100)
raul = BankAccount("Raul", 200)

doug.start()
paul.start()
raul.start()

doug.join() ### Wait for previous terminated
paul.join()
raul.join()









