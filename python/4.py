Birth_date= input('birth year: ')
print(type(Birth_date))
age = 2019 - int(Birth_date)
print(type(age))
print(age)

latter=''' Dear Name 
  how are u?
   Date ! '''
print(latter)
name= input("enter name ")
date = input("enter date ")
latter= latter.replace("Name",name)
latter= latter.replace("Date",date)
print(latter)