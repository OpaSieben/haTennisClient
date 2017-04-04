from client import Netcat
from time import sleep

cl = Netcat("80.74.140.117", 8888)
print cl.read_until("game?")
sleep(0.1)
cl.write('y')


print cl.read()
print cl.read()
print cl.read()

