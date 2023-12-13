print("hi bro how are you ") 
print(3+3)
print(5-10)
print(8*9)
print(4/5)
print(4//5)
print(10%2)
print(2**3)
print('hi bro\'s manohar is back')
print(r'c: \naven\manu')

a = 5
b = 10
print(a+b)
c = 2.3
d = a + b
print(d)

l = "lemnion"

print(l)
print(l[0])
print(l[5])
print(l[0:])
print(l[-1])
print(l[4:7])
print(l[1:])
print(l[:7])

h = []
my_num = ["2,5,10,2,3,22,65,56,89"]
my_name = "manohar"
print(len(my_name))
names = ["ravi","lion","manu","manoja","mummy","dad"]
print(names)
print(names[1])
print(names[2:5])
print(names[-1])
print(names.append("koney"))
print(names.insert(1,"Don"))
print(names)
names.extend(["koli","joker","girl","boy"])
names.pop()
names.pop(1)
names.remove("manoja")
#del names[2:]
print([my_num,my_name])
print(names)
my_num = [2,5,10,3,22,65,56,89]
my_num.sort()
print(my_num)
my_num.sort(reverse=True)
print(my_num)
print(max(my_num))
print(min(my_num))
print(sum(my_num))
h.append(my_num)
print(h)

#tuple = it is immutable and count index
tup = (21,56,35,2,1,5,2,8,1,1,1)
print(tup[1])
print(tup.count(1))
print(tup.index(8))

#set collection of unique elements : Never follows sequence 

f = {2,5,6,7,4,5,9,6}
print(type(f))
print(f)

num = [25,36,95,14,12,26]  #95,14,12

del num[2:5]

print(num)

data = {1:"ravi",2:"manu",4:"pop"}
print(type(data))
print(data[1])
print(data[4])
print(data.get(2))
#print(data.get(3))
print(data.get(1,"not found"))
print(data)

h = ['ravi','tarun','manu','rosie','manoja','iron']
j = ['java',"python","js","lion","joke","klm"]

fih = dict(zip(h,j))
print(fih)

print(fih['iron'])
fih["kulli"] = "laddu"
print(fih)

del fih['manoja']
print(fih)
del fih["kulli"]
print(fih)

a = 10
a =  b  
print(a)
print(b)
print(id(a))
print(id(b))
k = 10
print(id(k))

# we are noyt using K  that memoery wii be garbage collection 

PI = 3.14
print(PI)

PI = 3.15
print(PI)

c = 7+9j
print(type(c))
j = list(range(10))
print(j)

print(a)
a = 1.5
print(type(a))
print(int(True))
print(int(False))
print(int(a))
print(list(range(100)))
a = 2
b = 3
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)

c,d = 5,6
print(c)
print(d)

a = a+2
print(a)

a += 3
print(a)

b *= 5
print(b)

c *= 5
print(c)
print(a<b)
print(a>b)
print(a == b)
print(a != b)
print(a>5 and b>2)

k = True

k = not k
print(k)


z = False
z = not z
print(z)

print(bin(26))
print(0b0101)
print(oct(26))
print(hex(26))
print(0xf)

#swap the numbers 

a = 10
b = 30

'''temp = a
a = b 
b = temp'''

'''a = a+b 
b = a-b
a = a-b'''

'''a = a ^ b
b = a ^ b
a = a ^ b'''

a,b = b,a
print(a)
print(b)

a = 12
print(~a)

a= 14
b = 15
print(a & b)
print(a | b)
print(a ^ b)
print(10<<2)
print(10>>2)

import math
x = math.sqrt(25)
print(x)
v = math.pow(3,5)
print(v)
print(math.floor(2.9))
print(math.ceil(2.9))
print(math.pi)
print(math.e)

import math as m
z = math.sqrt(25)
p = m.sqrt(25)
print(p)
print(z)

from math import sqrt, pow

s =math.pow(5,6)
d = math.sqrt(50)
print(d)
print(s)

ma = input("Enter you are name")
print(f'im back my name is {ma}')
jk = eval(input("enter a expression"))
print(jk)

import sys
x = sys.argv[1]
y = sys.argv[2]
z = x + y 
print(z)

if True:
    print("I am Back")