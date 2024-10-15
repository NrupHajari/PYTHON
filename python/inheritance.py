# single inheritance
'''

class Empolyee:
    company="google"

    def showEmployee(self):
        print(f"empolyee company is {self.company}")
        

class Programmer(Empolyee):     # programmer class ma employee class add karel che
    language="python"

    def showProgrammer(self):
        print(f"programmer language is {self.language}")


'''
   # def showEmployee(self):                  # employee class attribute change  in programmer class  
 #  print("empolyee company is flipcart")
'''



#employee class 
 
nrup=Empolyee()
nrup.showEmployee()   # this print-->employ company is google
nrup.company="amazon"
nrup.showEmployee()  # change company 


# programmer class (but programmer class in employee class include  )
kano=Programmer()
kano.showEmployee()   # this print-->employ company is google( programmer ni andar employee ni details hoy atle aa pn print karse)
kano.showProgrammer()
'''


# MULTI INHERITANCE 
'''
class Employee:
    company="visa"
    ecode=120

class Freelancer:
    company="fiverr"
    level=3
    def upadatelevel(self):
        self.level=self.level+1
        print(self.level)


class programmer(Employee,Freelancer):  # 2 parents & 1 child . (EMployee) first lakhyu che programmer ni andar to priority employee hase
    name="nrup"        # baki jo Freelancer pela hoy to priority eni hot pela 

kano=programmer()
kano.upadatelevel()
print(kano.company)   # all time visa print because priority Employee ni che atle
                      #baki jo Freelancer pela hoy to priority eni hot pela  to print company-->fiverr hoy 
'''


#multilevel inherince  

class person:
    country="India"

    def people(self):
        print(f"i am {self.country}")

    def abc(self):
        print("hy i am boss !")

class employee(person):    # person is perents & employee is child
    company="google"

    def getsalary(self):
        print(f"{self.company} salary is rs {self.salary} ")

    def abc(self):
        print("hy i am boss & monster !")   # change class person - function(abc)
        
    

class programmer(employee):  # employee is perents & programmer is child but person is perents & employee is child then (dada,papa,apde)
    work="youtuber"
    def prgramming (self):
      print(f"he is programming in {self.work}")

    def abc(self):       # change employee class function (abc)
        print("nothing i am simple man !")

nrup=programmer()    # all class in programmer because person no chokro employee eno chokro programmer all DNA in programmer
nrup.salary=300
nrup.people()
nrup.getsalary()
nrup.prgramming()
print(nrup.country)
print(nrup.company)
print(nrup.work)



p=person()
e=employee()
pr=programmer()
p.abc()          # this print in person class 
e.abc()           # this print in empolyee class 
pr.abc()           # this print in programmer class 
                   # in case programmer class ma (abc) function nathi to ena najik na abc function print karavse (atle aa case ma employee na abc function ne )
                # in case employee class ma (abc) function nathi to ena najik na abc function print karavse (atle aa case ma person na abc function ne )
                # & person class ma abc function nathi to error throw 

