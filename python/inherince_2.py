# super inheritance  

class person:
    
    def abc(self):
        print("hy i am boss !")

class employee(person):    # person is perents & employee is child
  

    def abc(self):
        super().abc()   # pela perosn class nu abc function print thase 
        print("hy i am boss & monster !")   # change class person - function(abc)
        
    

class programmer(employee):  # employee is perents & programmer is child but person is perents & employee is child then (dada,papa,apde)
    

    def abc(self):       # change employee class function (abc)
        super().abc()   # pela employee class nu print karava jase but ema pn super() che atle person nu print karavi ne employee nu abc function print karse pacchhi programmer nu
        print("nothing i am simple man !")


p=person()
e=employee()
pr=programmer()
#p.abc()          # only person class nu abc function print thase 
#e.abc()          # aama super() che atle aa pela person class nu abc print karse pachhi employee class nu 
pr.abc()         # ama pn super() che to e employee class ma jase but tya bi super() che to person -> employee->programmer class na abc function print thase 


class Employee:
    company="bharat gas"
    salary=5000
    bonussalary=700
    
    @property
    def totalsalary(self):
        return self.salary+self.bonussalary
    
    @totalsalary.setter
    def totalsalary(self,val):
        self.bonussalary = val - self.salary

nrup=Employee()
print(nrup.totalsalary)

nrup.totalsalary=5200

print(nrup.salary)
print(nrup.bonussalary)

class number:
    def __init__(self,num):
        self.num=num 

    def __add__(num1,num2):
        print("lets add")
        return num1.num + num2.num
    def __str__(self):
        #print(f"decimal number {self.num}")
        return f"decimal number {self.num}"
    
n1=number(4)
n2=number(6)
sum=n1+n2
print(sum)
print(n1)
print(n2)


class vector:
    def __init__(self,vec):
        self.vec=vec 

    def __str__(self):
        str1=""
        index=0
        for i in self.vec:
            str1+= f"{i}a{index} +"
            index+=1 
        return str1[:-1]
    def __add__(vec1,vec2):
        newLists=[]
        for i in range(len(vec1.vec)):
            newLists.append(vec1.vec[i] + vec2.vec[i])
        return newLists
    def __len__(self):
        return len(self.vec)
        


v1=vector([1,4])
v2=vector([7,9])
print(v1)
print(v2)
s=v1+v2
print(s)
print(vector(v1+v2))
print(len(v1))
print(len(v2))

# represt vector  (in case vip means vector)(i ,j ,k carret ma )

class vip:
    def __init__(self,vip):
        self.vip=vip
    def __str__(self):
        return f"{self.vip[0]}i + {self.vip[1]}j + {self.vip[2]}"
kano=vip([1,4,7])
print(kano)