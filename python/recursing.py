# without recursing 
'''def factorial(n):
    product=1
    for i in range(1,n+1):
        product=product*i
    return product
f=factorial(4)
print(f)'''
# recursing function 

def factorial(n):
    if n==1 or n==0:
      return 1
    return n*factorial(n-1)
f=factorial(5)
print(f)

def sum(n):
   if n==0:
      return 0
   return n+sum(n-1)
s=sum(5)
print(s)