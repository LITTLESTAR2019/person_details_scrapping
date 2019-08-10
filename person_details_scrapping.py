#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests
from bs4 import BeautifulSoup
from __future__ import print_function
from bs4 import BeautifulSoup
from __future__ import print_function
import csv
if __name__ == '__main__':
    print("Enter the person name")
    n = raw_input()
    print(n)
    main_url="https://www.google.com/search?q=" +n

    result = requests.get(main_url)

if result.status_code==200: 
        print("Successfully opened the web page") 
        print("The details are as follow :-\n") 
        soup=BeautifulSoup(result.text,'lxml') 
        #print(soup.prettify())
        results=soup.findAll("div",{"class":"BNeawe s3v9rd AP7Wnd"})    
        #print(results)  
        records = []  
        for result in results:  
            details = result.text 
            records.append((details))
        print(records)

# Create a file to write to, add headers row
        f = csv.writer(open('details.csv', 'w'))
        f.writerow(['Name', 'Link'])
# Add each artist’s name and associated link to a row
        f.writerow([records])
else: 
        print("Error") 

