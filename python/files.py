# use open function to read the file ( pele thi save kari rakhavani)
f=open('sample.txt','r') # sample.txt peli thi save hati
data=f.read()
print(data)
f.close()

# new file banavi ne tema data add karva mate 
f = open('sample1.txt','w')  # sample1.txt new file bani aa function thi 
f.write("please write the file patel ")
f.close()