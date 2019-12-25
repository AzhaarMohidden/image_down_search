from bs4 import BeautifulSoup as soup
import urllib.request
import random
import numpy as np
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as Img
#urllib.request.urlretrieve("https://statics.cdntrex.com/contents/videos_screenshots/923000/923668/300x168/1.jpg?v=3", "a.jpg")

my_url = 'https://www.porntrex.com/categories/anal/'
containers_t="sdf"

uClient = urllib.request.urlopen(my_url)
page_html =uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")

containers = page_soup.findAll("img",{"class":"cover lazyload"})
containers_t = page_soup.findAll("p",{"class":"inf"})
#containers = page_soup.findAll("div",{"class":"video-list"})

def single_img(nu,ad):
	Img = containers[i]["data-src"]
	Img_url= str(Img).strip().replace("//","")
	print(Img_url)
	urllib.request.urlretrieve(ad, str(i) + ".jpg" )

def image_down(ad):
	for i in range(len(containers)):
	    Img = containers[i]["data-src"]

	    Img_url= str(Img).strip().replace("//","")
	    print(Img_url)
	    
	    urllib.request.urlretrieve(ad, str(i) + ".jpg" )

def loop_search():
    global containers
    global containers_t
    masters = 0
    for x in range(len(containers)):
        #m = str(z)
        Title = containers[x]["data-src"]
        Title1 = containers_t[x].a["title"]
        cat_tit = Title.split("/")
        cat_num = len(cat_tit)
        for l in range(cat_num):
            #print("cat_tit[l]: " + str(l) + " " + cat_tit[l])
            if l == 8:
            	p = str(cat_tit[8])
            	cat_tit_num=p.split(".")
            	for xp in range(1):
            		masters = masters +1 #print("slptnu : " + str(xp) + cat_tit_num[xp])
            		inc=1
            		while inc<9:
            			cat_tit_num[0] = str(inc)
            			hlf = cat_tit_num[0] + "." +cat_tit_num[1]
            			#print(hlf)
            			inc = inc +1
            			full = "https://"+cat_tit[2]+"/"+cat_tit[3]+"/"+cat_tit[4]+"/"+cat_tit[5]+"/"+cat_tit[6]+"/"+cat_tit[7]+"/"+hlf
            			print(full)
            			urllib.request.urlretrieve(full, Title1 +str(inc) + ".jpg" )
                        #urllib.request.urlretrieve(full, str(masters) + str(inc) + ".jpg" )
            			print("Added " + Title1 )
            			#single_img(x,full)
            			#image_down(full)
                    

loop_search()

