# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 18:57:42 2019

@author: Adil Ayub

NOTICE/PLEASE READ ME
Inputs:
Directory:This will take the directory name along with the html file as input.
folder_name:This will the output folder in which the images will be placed.

You may need to change how directories are created and deleted in the directories function cause it was made for
windows not linux.

"""

import urllib.request
from bs4 import BeautifulSoup
import os
import shutil

#get correct url from list
def find_http(lists):
    for data in lists:
        if(data[0:4] == "http"):
            return data
        
#create a directory to store images        
def directories(location,foldername):
    file_path=location.split("\\")
    filename=location.replace(file_path[len(file_path)-1],foldername)   
    #print(filename)
    
    if os.path.exists(filename):
        shutil.rmtree(filename, ignore_errors=True)
        
    for retry in range(100):
        try:
            os.mkdir(filename)        
            break
        except:
            print ("Failed to Create folder hence exiting . Please try again")
            exit()
    print(filename + ' is created with the images.')
    return filename

#downloading images and adding to folder 
def add_images(foldername,urls):
    index=1
    for url in urls:
        '''
        if((url[len(url)-3:len(url)] == "jpg") or (url[len(url)-3:len(url)] == "png")):
            formats=url[len(url)-3:len(url)]
        elif(url[len(url)-4:len(url)] == "jpeg"):
            formats=url[len(url)-4:len(url)]
        else:
        '''    
        formats=".png"
        new_file_name=foldername+"\\filename-"+str(index)+"."+formats
        try:
            urllib.request.urlretrieve(url,new_file_name)
            print(str(index)+"/"+str(len(urls))+" have been downloaded.")
        except:
            print(str(index)+"/"+str(len(urls))+" failed to be downloaded.")
        index=index+1    
        
    print("Download has been completed")
    
imagesurls=[]
split_url=[]
folder_name="Batman"
directory=r"D:\University\FYP\Data-set\batman - Google Search.htm"
new_dir=directory.replace("\\","\\\\")
file=open(new_dir,'r')

#parsing for data
soup = BeautifulSoup(file, 'html.parser')
all_images=soup.find_all("div", class_="rg_bx rg_di rg_el ivg-i")
for images in all_images:
    temp=images.find_all("div", class_="rg_meta notranslate")
    for img in temp:
        imagesurls.append(img)
        
#print(imagesurls[1])
#getting the urls        
for url in imagesurls:
    split_temp=str(url)
    split_temp=split_temp.split("\"")
    split_url.append(find_http(split_temp))

folder_name=directories(directory,folder_name)   
add_images(folder_name,split_url) 
'''    
'''     
'''   
index=0
for data in split_temp:
    print("Index is "+str(index)+"\n"+data)
    index=index+1   

index=0
for data in split_url:
    print("Index is "+str(index)+"\n"+data)
    index=index+1
'''    
#print(split_temp[29])    
#print(soup.prettify())
    
