import sys

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

for i in range(1,100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000):
    num = num*2
    print(num)