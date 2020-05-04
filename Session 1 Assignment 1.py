#!/usr/bin/env python
# coding: utf-8

# # Task 1:

# In[ ]:


# 1. Install Jupyter notebook and run the first program and share the screenshot of the output. LINK

# https://www.anaconda.com/products/individual#windows


# In[8]:


# 2 Write a program which will find all such numbers which are divisible by 7 but are not a multiple
# of 5, between 2000 and 3200 (both included). The numbers obtained should be printed in a
# comma-separated sequence on a single line.

dm=[]
for x in range(2000, 3200):
    if (x%7==0) and (x%5==0):
        dm.append(str(x))
print (','.join(dm))


# In[19]:


# 3. Write a Python program to accept the user's first and last name and then getting them printed in 
# the the reverse order with a space between first name and last name.

a = "Santhosh Reddy"
print(a)
print (a[::-1])


# In[ ]:


# 4 Write a Python program to find the volume of a sphere with diameter 12 cm. Formula: V=4/3 * π * r 3
# Not sure about the question


# # Task 2:

# In[22]:


# 1. Write a program which accepts a sequence of comma-separated numbers from console and generate a list.
list = (1,2,3,4,5,6)
list


# In[36]:


# 2. Create the below pattern using nested for loop in Python.
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

nl = ''
for i in range (0,9):
    if i <5:
        nl = nl +"*"
        print(nl)
    elif i >4:
        nl = nl[:-1]
        print(nl)


# In[64]:


# 3 Write a Python program to reverse a word after accepting the input from the user.
#Sample Output:
# Input word: AcadGild
# Output: dilGdacA

rev = "Santhosh"
rev = (rev[::-1])
rev


# In[90]:


# 4 Write a Python Program to print the given string in the format specified in the sample output.
# WE, THE PEOPLE OF INDIA, having solemnly resolved to constitute India into a
# SOVEREIGN, SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC and to secure to all
# its citizens

# Sample Output:
# WE, THE PEOPLE OF INDIA,
# having solemnly resolved to constitute India into a SOVEREIGN, !
# SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC
# and to secure to all its citizens

print ("WE, THE PEOPLE OF INDIA,\nhaving solemnly resolved to constitute India into a SOVEREIGN,! \nSOCIALIST, SECULAR, DEMOCRATIC REPUBLIC \nand to secure to all its citizens")

