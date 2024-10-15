a="good morning, "
b='nrup'
c=a+b     # two ya many variable concatenating string 
print(c)
print(b[0])
print(b[1])
print(b[2])
print(b[3])   # b[1]=g --> does not change/work 

print(b[0:3])  # [0:3]= only print 0,1,2 not print 3 in python 
print(b[1:4])  # [0:4]= only print 1,2,3 not print 4 in python

print(b[:3])  # is same print(b[0:3]) --> output is start is 0
print(b[0:])  # is same output print(b[0:4])--> output is end  (in case n=0,r=1,u=2,p=3 ) 

d="pqrstuvwxyz" # print[0:11] total 11 char but start with 0 , end 10 but pyathon [0:10] print 0 to 10 ,not print 11
c=d[0:7:2]  # first (:) is limit and second (:) is skip the word in case [0:7] print but all 2 charater skip and output is prtv
print(c)
e=d[0::3] # first print [0:] = print[0:11] & second(:) skip charand print char after 3 run then output is psvy
print(e)

story="I am is nrup hajari.I am student." # all char & symbol(.) & space is count in length 
print(len(story)) # find the length 
print(story.endswith("student.")) # true or false --> to end which word 
print(story.count("a"))  # count the char is variable always write in (" "),(' ')
print(story.capitalize()) # capital to first word to first char
print(story.find("nrup")) # find the word in which location ( length pr che ) & always first word find in string not same second word
print(story.find("kano")) # word in not string then output is -1
print(story.replace('nrup','patel')) # replace word nrup to patel ( all nrup word0 change in string )
