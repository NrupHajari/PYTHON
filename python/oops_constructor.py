'''
class Employee:
    company ="google"
        
                 
    def __init__(self,name,salary,subunit):
        self.name= name 
        self.salary=salary
        self.subunit=subunit

        print("Employee is crated!")       # this line print by __init__ constuction
       

    def getdetail(self):
      print(f"the employee name is {self.name} and salary is {self.salary} and subunit is {self.subunit}")   # this line print by kano,1000,programmer

    def getsalary(self,sing):
        print(f"salary is {self.salary} and working in {self.company}\n{sing}")
    
    @staticmethod
    def greet():   # greet(self)--> throw error (self no use na karvo hoy to @staticmethod use karvo)
         print("good morning sir ,") 

nrup=Employee("kano",1000,"programmer")   # without("kano",1000,"programmer ")--> error throw 
nrup.getdetail()  '''




class calculater:
    
    def __init__(self,num):
        self.number=num
    def spuare(self):
        print(f"value of {self.number} square is {self.number**2}")
    def cube(self):
          print(f"value of {self.number} cube is {self.number**3}")
        
    @staticmethod
    def greet():
         print("******welcome*******")

a=calculater(3)
a.greet()
a.spuare()
a.cube()




class sample:
     name="nrup"   # class attribute 

b=sample()
b.name="kano"   # instance attribute

print(sample.name)   # print from sample class name --> nrup
print(b.name)        # but this print --> kano , change the class aatribute 
  # change class attribute
sample.name="patel"

print(sample.name)