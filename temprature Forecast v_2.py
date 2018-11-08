#!/usr/bin/env python
# coding: utf-8

# In[5]:


# importing basic library used in the program
import re
import time
import urllib.request 


# ### https://www.weather-forecast.com/locations/Paris/forecasts/latest
# #### This is the site used for the required information

# In[6]:


print("Input Me with Capital of the Country and I will provide you with Temprature of the country\n")

usr_input =(input("What is your input : "))
usr_input = usr_input.strip()

# Concatenating url with the user input
url = 'https://www.weather-forecast.com/locations/' + usr_input + '/forecasts/latest'


# In[7]:


try:
    # Reading data for the url Created above
    data = urllib.request.urlopen(url).read()
    
    # decoding data to utf-8 format
    data_decode = data.decode('utf-8')
    
    #finding the string " phrase"> " in the source code of above url and the saving the output in a varable  :find_data:
    find_data= re.search('phrase">', data_decode)

    # Again searching for string '.</span></p>' in the source code
    new_data  = re.search('.</span></p>',data_decode)


    # saving starting points and ending points of the of the above collected data in some variable 
    s = new_data.start()
    e = new_data.end()
    #print(s, e)

    start = find_data.end()
    end = find_data.end() +100
    #print(start, end)
    
    usr_input = usr_input.upper()
    
    print("\n-----------------------------------------")
    print("-----TEMPRATURE------------" + usr_input + "------\n")
    print('Temprature in ' + usr_input  + ' Currently is >> '  + data_decode[start: s] )
    
    time.sleep(10)
    
except: 
    print('\n')
    print('-------------------------------------')
    print('Sorry your City is not in our List : ')
    print('-------------------------------------')
    time.sleep(5)


# In[ ]:




