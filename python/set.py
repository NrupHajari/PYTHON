a={1,3,6,5}   # in set alway ordering form output
print(type(a))
print(a)

g={ 18, "18", 18.1,18.0}  # all data type print in set 18 is int , "18" is string , 18.1 is float 
print(g) # 18.0 is float but 18 is present & only one time 18 
print(len(g))

b={1,2,3,5,4,1} # not print same value in case 1 only 1 time print in set 
print(type(b))
print(b)

# imporant= this syntax will create an empty dictionary and not an empty  set
c={}
print(type(c))  # output is <class.'dist'>  not set type 
print(c)

# create empty set below syntax
d=set()
print(type(d))
print(d)

d.add(3)  # add in set 
d.add(5)
d.add(4)
d.add(3)  # but set is non repetive element ony one time 3 add 
d.add((1,2,3)) # tuples add in set but list not add in set . [1,2,3]-->list is not add in set. disctiony not add in set {1,2,3}
print(d)
print(len(d))
d.remove(4) # remove 4 in set 
# d.remove(17) --> error through (not present in set)
print(d)
print(d.pop())  #remove an arbitary element from set and return remove element 
print(d)