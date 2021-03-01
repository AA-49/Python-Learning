#Data-Types-&-Operator
print(5+5)
print(5-5)
print(5*2)
print(5**2)
print(5/2)
print(5//2)
print(5%2)

#Give data
number=1,2,3,4,5,6,7,8
print(number)
print(number[0])
print(number[4])

#Types Save Data ( del )

#Types-int-&-float
#int=60
#float=60.9
print(int(20.5))
print(int(20))
print(float(20.5))
print(float(20))

#bool = Boolean
#show true & false
x=30
print(x<1)
print(x>1)

#Comparison Operators
less_than = 1<2
greater_than = 2>1
lesser_than_equal = 1<=1.5
greater_than_equal =  2>=1.5
equal_to = 1==1
not_equal_to = 1!=9

#logical Operators
#and = both true
#or = At least one side true
#not = inveres a boolean type

#len()
print(len('andy'))

#number cannot used

#Types
print(type(20))
print(type(20.5))
print(type('20.5'))
print(type("20.5"))

#Title
print('andy chu'.title())
print("andy chu".title())

#Islower
name = 'andy chu'
print(name.islower())

#Count
print('2,3,1,11,22,4,1,1'.count('1'))
print("fish,cow,cat,fish".count("fish"))
#Must be in str()formet

#Data Contaner 1) list
#max() & minn()
listA= 'a','b','c'
a=10
b=a+1
c=b+1
print(max(listA))
print(min(listA))
listB= 1,2,3,4,5,6,7,8,9
print(max(listB))
print(min(listB))
#sorted()-small to big
sizes=[5,6,7]
print(sorted(sizes))
print(sorted(sizes,reverse = True))
#join()
x="\n".join(['x','y','z'])
print(x)
y='/'.join(['z','y','x'])
print(y)
z=['a','b','c']
print('-'.join(z))
#The ' '.join can be use in or out
#append()
a=['w','x','y']
a.append('z')
print(a)

#Data Contarner 2)Tuple

#Data Contarner 3)Set
ABC='alan','andy','evon','alan','andy','andy'
ABC_Set=set(ABC)
print(len(ABC_Set))
print('andy'in ABC)
print('andy'in ABC_Set)
#not use append() use add()
#pop()-choose one to mines

#Data Contarner 4)Dictionary
elements={'hydrogen':1 , 'helium':2}
print(elements['hydrogen'])
elements['carbon']=6
print(elements)
print(elements.get('carbon'))
print(elements.get(6))

# END