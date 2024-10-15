'''class Employee:
    company ="google"
    def getsalary(self):
        print(f"salary is {self.salary} and working in {self.company}")

nrup=Employee()
#nrup.salary()    # nrup.salary()==Employee.salary(nrup)
#Employee.salary(nrup)
nrup.salary =500
nrup.getsalary()'''


class Employee:
    company ="google"
    def getsalary(self,sing):
        print(f"salary is {self.salary} and working in {self.company}\n{sing}")
    
    @staticmethod
    def greet():   # greet(self)--> throw error (self no use na karvo hoy to @staticmethod use karvo)
         print("good morning sir ,")

nrup=Employee()
#nrup.salary()    # nrup.salary()==Employee.salary(nrup)
#Employee.salary(nrup)
nrup.salary =500
nrup.getsalary("thanks!")
nrup.greet()   #Employee.greet() == nrup.greet()
#Employee.greet()