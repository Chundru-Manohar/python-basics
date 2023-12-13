'''if False:
    print("iam back")
print("good bye")

#postive number or negative number

num = float(input("Enter a number: "))

if num>0:
    print("postive number")
elif num == 0:
    print("zero")
else:
    print("negative number")

# take 3 values from user which value is greater 

a = float(input("Enter a first number "))
b = float(input("Enter a second number "))
c = float(input("Enter a third number "))

if a>b and a>c:
    print("a is greater")
elif b>a and b>c:
    print("b is greater ")
elif c>a and c>b:
    print("c is greater ")'''


'''counter = 10
while counter>=1:
    print("manohar is a back",counter)
    j = 1
    while j <= 5:
        print("cute boy ")
        j += 13
    counter -= 1


g = [ "manu",5,"lion"]

print(g)
for i in g:
    print(i)

for i in range(1,11,1):
    if i %5 != 0:
        print(i)

#break pass continue  

f = int(input("Enter a number "))
av = 10
h = 1
while h<= f:
    if h>av:
        print("out of stock")
        break
    print("manohar is a good boy ")
    h += 1

print("red")
'''
'''for i in range(1,51):
    if i % 5 ==0 or i % 3 ==0:
        continue
    print(i)'''

'''for u in range(1,101):
    if (u %2)!= 0:
        pass
    else:
        print(u)

# check number is prime or not 

#A prime number is a natural number greater than 1 that is not a product of two smaller natural numbers.
#Any whole number which is greater than 1 and has only two factors that is 1 and the number itself, is called a prime number

def prime_num(num):
    if num  <= 1:
        return False
    elif num >= 2:
        return True
    elif num % 2 == 0:
        return False
    else:
        for i in range(3,int(num*0.5)+1,2):
            if num % i == 0:
                return False
        return True
num = int(input("Enter a number: "))
if prime_num(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")'''

'''for t in range(5):
    if t == 3:
        continue
    print(t)

for u in range(10):
    if u ==5:
        break
    print(u)

for z in range(10):
    if z ==5:
        pass
    print(z)'''
'''
print(" * ",end='')
print(" * ",end='')
print(" * ",end='')
print(" * ",end='')'''
'''
for j in range(4):
    print(" * ",end='')
print()
for j in range(4):
    print(" * ",end='')
print()
for j in range(4):
    print(" * ",end='')
print()
for j in range(4):
    print(" * ",end='')
print()'''

'''for i in range(4):
    for j in range(4):
        print(" # ",end='')
    print()'''
'''
for i in range(4):
    for j in range(i+1):
        print(" * ",end="")
    print()

for i in range(4):
    for j in range(4-i):
        print(" *0 ",end='')
    print()
 
h = [1,3,5,7,2]

for i in h:
    if i %2 == 0:
        print(i)
        break
else:
    print("not found")'''


'''a = 7

for p in range(2,a):
    if a % p ==0:
        print("not prime")
else:
    print("its prime")'''

j = int(input("Enter a number "))

for k in range(2,j):
    if j % k ==0:
        print("not a prime number")
        break
else:
    print("its prime number")
import array

ma = array.array('i', [2,4,5,8,10,2,1])
print(ma)
print(ma.typecode)
print(ma.buffer_info())
ma.reverse()
print(ma)

for y in range(len(ma)):
    print(ma[y])

for t in ma:
    print(t)


klm = array.array(ma.typecode, (a*a for a in ma))
print(klm)

bm = [g for g in ma]
print(bm)