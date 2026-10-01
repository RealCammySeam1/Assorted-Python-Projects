import sys
import threading
from decimal import *

getcontext().prec = 100000000000000000
sys.set_int_max_str_digits(0)

print(1)
print(2)
print(3)
print(4)
print(5)

print("---- Using for loop ------")
for i in range (0,10,2):
    print(i)



#for i in range (start, end, count by)

print("Counting down")
for i in range(10,1,-1):
    print(i)

num = 1
def makeHugeNumber():
    global num
    for i in range(1,100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000):
        num = num*220394875239847590723507238970795743564576067646243156471093287421340912384601923785021937580122340975293046502101570892347558069
        print(num)

makeHugeNumber()

t1 = threading.Thread(target=makeHugeNumber, args=(4,))
t2 = threading.Thread(target=makeHugeNumber, args=(4,))
t3 = threading.Thread(target=makeHugeNumber, args=(4,))
t4 = threading.Thread(target=makeHugeNumber, args=(4,))
t5 = threading.Thread(target=makeHugeNumber, args=(4,))
t6 = threading.Thread(target=makeHugeNumber, args=(4,))
t7 = threading.Thread(target=makeHugeNumber, args=(4,))
t8 = threading.Thread(target=makeHugeNumber, args=(4,))

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
t7.start()
t8.start()

t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
t6.join()
t7.join()
t8.join()