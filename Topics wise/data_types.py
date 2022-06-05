a=4
print(type(a))                        #int
print(int(a))
print(float(a))
print(str(a))
#print(tuple(a))                           #not possible to tuple
print(bool(a))
#print(set(a))                             #not possible to set

a = 5.5
print(type(a))                        #float
print(int(a))
print(str(a),type(str(a)))
print(bool(a))
#print(tuple(a))                             #cant convert to tuple

a="9"
print(type(a))                        #number as string
print(bool(a))
print(int(a))
print(float(a))
a="string"
print(type(a))                        #string
print(bool(a))
#print(int(a))                               #cant to int
#print(float(a))                             #cant to float

a=False
print(type(a))                        #boolean
print(int(a))
print(float(a))
print(str(a))
#print(tuple(a))                             #cant to tuple

a=(1,2,8,7,90,87,4,8)
print(type(a))                        #tuple
print(a[0],a[2])
print(set(a))                                #sorting the tuples and removes duplicates
print(list(a))
print(bool(a))
#print(int(a))                               #cant to int
#print(float(a))                             #cant to float

a={1,2,8,7,90,3,1}
print(type(a))                        #set
#print(a[0])                               # Error set not subscriptabel
print(tuple(a))                                #sorting the tuples and removes duplicates
print(list(a))
print(bool(a))
#print(int(a))                               #cant to int
#print(float(a))                             #cant to float

a=[1,2,8,90,89,7]
print(type(a))                        #list
print(a[0],a[2])
print(tuple(a))
print(set(a))                                #sorting the tuples and removes duplicates
#print(int(a))                               #cant to int
#print(float(a))                             #cant to float

a=((1,2),5,7.0,(8,90),9,5,4)
print(type(a))                        #tuple
print(a[0])                                #result (1,2)
print(a[0][1],a[0][0],a[3][1])             #result 2,1,90
print(list(a))
print(set(a))                                #sorting the tuples and removes duplicates

a={(1,2),5,7.0,9,8,2}
print(type(a))                        #Set
print(tuple(a))
print(list(a))                                 #sorting the tuples and removes duplicates