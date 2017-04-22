import threading
import time

class AsyncThread(threading.Thread):

    def __init__(self, text, out):
        threading.Thread.__init__(self)
        self.text = text
        self.out = out
    
    def run(self): ### method inside threafing
        f = open(self.out, "a")
        f.write(self.text+'\n')
        f.close()
        time.sleep(2)
        print("Finished background file write to "+self.out)


def main():
    message = input("Enter a string to store: ")
    background = AsyncThread(message, 'out.txt')
    background.start()

    print("The program can continue whilte it's writting in another thread")
    
    background.join()
    print("Waited until thread was completed")

if __name__=='__main__':
    main()