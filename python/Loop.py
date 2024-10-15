# while loop
'''i=1
while i<=50:
    print( str(i))
    i=i+1 
 
i=0
while i<5:
    print("nrup " +str(i))
    i=i+1'''

# for loop
'''l=[1,2,4,3]
for iteam in l:
    print(iteam)

for i in range(8):  # range function print --> 0 to 7
    print(i)

for j in range(1, 8): # print --> 1 to 7
    print(j)

for k in range(2, 16, 3):  # strat 2 to 15  but print next 3 step -->2,5,8,11,14 
    print(k) '''

'''for i in range(10):
    print(i)
    if i==5:
        break
else:
    print("done")'''


# continue 
'''for i in range(10):
    if i==5:          # continue = jo condition true thay to skip kari ne agad vadhe 
        continue      # in case i=5 thay atle 5 ne skip kare --> 0,1,2,3,4,6,7,8,9
    print(i)'''

# pass statement
'''i=4
if i>0: 
    pass
while i>6:
    pass
print(" nrup ")  # without pass program error through

j=1
num=int(input("enter number: "))
while j<11:
    print(str(j*num))
    j=j+1

if (num%2)==0:
    print("even")
else:
    print("odd")

sum=0
for k in range(1,num+1):

   sum=sum+k
print(sum)        # print(sum)  always for ni line niche avse toj badha no sum thase baki judu judi line ma avse 

factorial=1
for k in range(1,num+1):
    factorial=factorial*k 
print(factorial)'''


# pattern in python 
'''num=int(input("enter number: "))
for i in range(1,num+1):
    print("*" * i)

for i in range(1,num+1):
    print(" " *(num-i),end="")
    print("*" * (2*i - 1) , end="")
    print(" " *(num-i))  '''


# revers print multiple table 
n=int(input(" number : "))
for i in range(10,0,-1):
    print(i*n)
