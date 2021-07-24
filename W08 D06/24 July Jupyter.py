#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# collections--- in python

#  deque ---is double ended queue
# append, appendleft, extend, extendleft, pop , popleft,
# FIFO : First in First out(queue)
# LIFO : drque
#  Counter -  Gives you a count of each items in the container with key value structure
#  OrderedDict
#  ChainMap




#  datetime



# In[ ]:


import collections
dq = collections.deque([4,5,6])
print(dq)

dq.append(7)
print(dq)

dq.appendleft(3)
print(dq)

dq.extend([8,9])
print(dq)

dq.extendleft([2,1,0])   #[1,0]
print(dq)

dq.insert(4,-10000)
print(dq)

dq.pop()
print(dq)

dq.popleft()
print(dq)


# In[ ]:


a = [1,2,3,4]
a = collections.deque(a)
a.extendleft(['A','B'])
print(a)


# In[ ]:


L1 = ['x','y','z','z','z','z','x','z']

print(collections.Counter(L1))

S1 = @
print(collections.Counter(S1))
# most common
#print(collections.Counter(L1).most_common(1))

#elements---iterable object
E = collections.Counter(L1)
for i in E.elements():
    print(i)


# In[ ]:


# OrderDict ----order of insertion in Dict Py 2.7 was not taken care of
# but in 3 and above it there.

a = {'apple':3,'mango':4}
OD = OrderedDict(a)
OD


# In[ ]:


OD.keys()
OD.values()


# In[ ]:


from collections import OrderedDict
OD = OrderedDict({ 'Randy Orton': 'Red', 'Dwayne Johnson' : 'Blue', 'Jhon Cena':'Red' })
print(OD)
OD.move_to_end('Dwayne Johnson')
print(OD)


# In[ ]:


from collections import ChainMap

d1 = {'a':1,'b':2}
d2 = {'c':1,'d':2}
d3 = {'e':1,'f':2}

C = ChainMap(d1,d2,d3)
C


# In[ ]:


FMCG = {'soap':3,'shampoo':4}
PANTRY = {'floor':5,'lentils':6}
OI = {'TV':1,'Batteries':2}


C = collections.ChainMap(OI,FMCG,PANTRY)
print(C)


print(list(C.keys()))
print(list(C.values()))


# new_child
c= {'zshoe':2,'socks':3}
C = C.new_child(c)
print(C)


# In[ ]:


# substring and string
String = 'my name is bikash s'               
String.count('s')





# In[ ]:


# datetime HH:MM:SS hh:mm:ss DD/MM/YY

# inside datetime i have few important classes
# time
# date
# datetime


# In[ ]:


import datetime as dt

x = dt.datetime.now()
x 

print(x.month)
print(x.day)

y = dt.date.today()
print(y)

from datetime import time


z = time(hour = 8, minute = 51, second = 30)
print(z)


from datetime import datetime
z1 = datetime(2021,7,24,8,54,30)
print(z1)


# date(y,m,d)
# time(h,m,s,microseconds)
# datetime(y,m,d,h,minute,s,microseconds)
import datetime as dt


# In[ ]:


import datetime as dt

# Write a Python script to display the various Date Time formats.
# a) Current date and time
# strftime is used to format our time into string format


print(dt.datetime.now())

# b) Current year

D = dt.date.today()
D.strftime("%Y")
#string format time

# c) Month of year
D.strftime("%m")

# d) Week number of the year
D.strftime("%W")

# e) Weekday of the week
print(D.strftime("%A"))

# f) Day of year

D.strftime("%j")
# g) Day of the month
D.strftime("%d")


# h) Day of week

D.strftime("%w")


# In[ ]:


from collections import ChainMap 
 
x = {'Age': 10, 'Name': 'Vinii'} 
y = {'Gender': 'Female'} 

X = ChainMap(x, y)
print ("Values associated with the keys of Chainmap: ") 
print (list(X.maps)) 

X


# In[ ]:


contestants = { 'Randy Orton': 'Red', 'Dwayne Johnson' : 'Blue' }
contestants['Jhon Cena'] = 'Red'
contestants


# In[ ]:


from collections import OrderedDict
OD = OrderedDict({ 'Randy Orton': 'Red', 'Dwayne Johnson' : 'Blue', 'Jhon Cena':'Red' })
print(OD)
OD.move_to_end('Dwayne Johnson')
print(OD)

OrderedDict(reversed(list(OD.items())))


# In[ ]:


Write a Python script to display the various Date Time formats.
a) Current date and time
b) Current year
c) Month of year
d) Week number of the year
e) Weekday of the week
f) Day of year
g) Day of the month
h) Day of week


# In[ ]:


#There is a difference between datetime.strp[arse]time() and datetime.strf[ormat]time().

#The first one, strptime() allows you to create a date object from a string source, 
#provided you can tell it what format to expect:

strDate = "11-Apr-2019_09:15:42"
dateObj = datetime.strptime(strDate, "%d-%b-%Y_%H:%M%S")

print(dateObj)


#The second one, strftime() allows you to export your date object to a string in the format 
#of your choosing:


dateObj = datetime(2019, 4, 11, 9, 19, 25)
strDate = dateObj.strftime("%m/%d/%y %H:%M:%S")

print(strDate)



# In[ ]:


from datetime import datetime
date_object = datetime.strptime('July 1 2014 2:43PM', '%B %d %Y %I:%M%p')
print(date_object)


# In[ ]:


OI = {'TV':1,'Batteries':2}
FMCG = {'soap':3,'shampoo':4}
PANTRY = {'floor':5,'lentils':6}

C = collections.ChainMap(OI,FMCG,PANTRY)
print(C)


print(list(C.keys()))
list(C.values())

