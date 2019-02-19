#!/usr/bin/env python
# coding: utf-8

# In[10]:


#Importing the Essential Libraries
import urllib.request
import re
import pyautogui as pag

def main():
    restart = 'Restart'
    while restart == 'Restart':
        try:
            #getting the input for the user 
            user_input = pag.prompt(text='Enter Your Word :', title = 'Dictionary 2.0').strip()

            #Mixing the user input with Required Url
            url = 'https://www.dictionary.com/browse/' + user_input

            #Getting the data form the url and decoding it to Utf-8 format
            data = urllib.request.urlopen(url).read().decode('utf-8')

            #Locating the Defination from the data
            stringStart = re.search('<meta name="description" content="', data)
            stringEnd = re.search('See more.">', data)

            start = stringStart.end() + len(user_input) + 13
            end = stringEnd.start() - 2

            defination = data[start:end]

            # Printing the results
            prompt = 'The Defination of {} is : {}'.format(user_input.upper() , defination.upper())
            restart = pag.confirm(text= prompt, title='Dictionary 2.0',buttons=['Quit', 'Restart'])

        except:
            restart = pag.confirm(text='Required Word is not in our Dictionary', title='Dictionary 2.0' ,buttons=['Quit' , 'Restart'])
            
if __name__ == '__main__':
    main()   