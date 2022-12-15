#!/usr/bin/env python
# coding: utf-8

# In[1]:


num = int(input("Enter a number: "))
if (num % 2)==0:
   print("{0} is Even".format(num))
else:
   print("{0} is Odd".format(num))


# In[4]:



year = int(input("Enter the year: "))
if (year % 400 == 0) and (year % 100 == 0):
    print("{0} is a leap year".format(year))
elif (year % 4 ==0) and (year % 100 != 0):
    print("{0} is a leap year".format(year))
else:
    print("{0} is not a leap year".format(year))


# In[ ]:




