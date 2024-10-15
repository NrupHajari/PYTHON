mydict={
    "nrup":"hajari ",   # nrup , kano , marks ,abv,1 are keys 
    "kano":"patel",     # hajari , patel ,[1,2,3] , 2 --> values
    "marks":[1,2,3],
    "abv": {'Nrup':'player'}, # dictionary in dictionary 
    1: 2
}
print(mydict['nrup'])
print(mydict["marks"])
print(mydict["abv"])
print(mydict["abv"]['Nrup'])

# dectionary methode 

print(mydict.keys())  # all keys in output 
print(list(mydict.keys())) 

print(list(mydict.values()))  # all values in output

print(mydict.items())  # print keys & values all

print(mydict.get("nrup")) # print value 
print(mydict["nrup"]) 

print(mydict.get("nrup2")) # not key in dectionary but return --> None
print(mydict["nrup2"])  # not key in dictionary error through