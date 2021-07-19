from time import sleep
from threading import *
class hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello")
            sleep(1)


class hi(Thread):
    def run(self):
        for i in range(5):
            print("HI")
            sleep(1)

h1=hello()
sleep(.002)
h2=hi()

h1.start()
h2.start()

h1.join()
h2.join()
print("BYE")
