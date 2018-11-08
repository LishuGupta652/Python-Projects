#!/usr/bin/env python
# coding: utf-8

# In[86]:


import re 
import urllib.request
import time
#https://www.dictionary.com/browse/-----


# In[87]:


print("________Welcome to Dictionary 2.0___________\n")


# In[88]:


usr_input = input("What do you want to Define: ")
usr_input = usr_input.strip()
url = 'https://www.dictionary.com/browse/' + usr_input


# In[102]:


try:
    data  = urllib.request.urlopen(url).read()
    data_decode = data.decode('utf-8')
    
    
    dis_data = re.search('<meta name="description" content="',data_decode)
    s = dis_data.start()
    e = dis_data.end()

    end_data = re.search('See more."', data_decode)
    e_s  = end_data.start()
    e_e = end_data.end()


    #caluculating lenght of user input 
    lenght_usr_input = len(usr_input) + 13 + e
    
    defination  = (data_decode[lenght_usr_input : e_s])
    
    usr_input = usr_input.upper()
    
    print("\n-----------------------------------------")
    print("-----DICTIONARY------------" + usr_input + "------\n")    
    print("THE DEFINATION OF --  " + usr_input + " -- can be Defined as : "  + defination)
    
    time.sleep(10)
except: 
    print("\n")
    print("----------------------------------------")
    print("Sorry your Word is not in out Dictionary")
    print("----------------------------------------")
    time.sleep(5)

