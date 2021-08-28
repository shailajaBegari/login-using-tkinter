details={
    "name":"Shanti",
    "age":12,
    "email":"shanti@navgurukul.org",
    }

print(details["name"])
print(details["email"])
print(details['age'])
print('___________________________________')
dict1={1:2,2:3,3:4,4:5}
sum=0
for i in dict1.values():    
    sum=sum+i
print(sum) 
print('___________________________________________')
c=dict()
for i in range(1,16):
    c[i]=i*i
print(c)  
print('_______________________________________')
s={'umesh':21,'bijender':54,'amar':67,'peter':89,'sonu':56}
a={'python':20,"gaurav":300,'dev':34,"karan":43}
for i in (s,a):
    s.update(a)
print(s) 
#{'umesh':21,'bijender':54,'amar':67,'peter':89,'sonu':56,'python':20,"gaurav":300,'dev':34,"karan":43}