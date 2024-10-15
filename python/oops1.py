'''
class Number:        # class 
    def sum(self):
        return self.a+self.b

num=Number()   #object 
num.a=5
num.b=7
s=num.sum()
print(s)


class RailwayForm:
    # formType="RailwayFrom"
    def formtype(self):
        print(f"name is {self.name}")
        print(f"train is {self.train}")

nrupApplication=RailwayForm()  # object - nrupApplication (all details to nrupApplication like name,train...)
nrupApplication.name="Nrup"
nrupApplication.train="abc"
nrupApplication.formtype()
                              '''

class Employee:
    company="google"   # aa class attribute kevay
    salary=100          # aa class attribute kevay
nrup=Employee()
kano=Employee()
patel=Employee()    # patel,kano,nrup ni company&salary hoy to pela e print thay na hoy to class attribute ma thi le 
patel.company="abcd" # (instance attribute) # patel ni company  apeli che to all time aaj print thase class aattribute mathi nai le 
nrup.salary=500    #(instance attribute)  # but patel ni salary apeli nathi to e class attribute ma thi lai print karave
kano.salary=300     # aa instance attribute kevay
print(nrup.company)
print(kano.company)
print(patel.company)
Employee.company="amazon"  # change the class attribute(with class(employee) )
print(nrup.company)
print(kano.company)
print(patel.company)

print(nrup.salary)   # nrup ,kana ni salary apeli che to e j print karse aane instance attribute
print(kano.salary)
print(patel.salary)   # aa salary class attribute mathi le se 

# below line throw error because address not present in instance/ class attribute 
print(nrup.address)  # pela object(nrup) ma joyu address che nathi pacchi class attribute ma joyu ema pn nathi to error through