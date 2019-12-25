import numpy as np
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as Img
from bs4 import BeautifulSoup as soup
import urllib.request
import random
my_url = 'https://www.porntrex.com/categories/anal/'
containers_t="sdf"

uClient = urllib.request.urlopen(my_url)
page_html =uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")

containers = page_soup.findAll("img",{"class":"cover lazyload"})
containers_t = page_soup.findAll("p",{"class":"inf"})

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
	masters= 0
	for x in range(len(containers)):
		Title = containers[x]["data-src"]
		Title1 = containers_t[x].a["title"]
		cat_tit =Title.split("/")
		cat_num =len(cat_tit)
		p=str(cat_tit[8])
		cat_tit_num =p.split(".")
		inc = 1
		while inc<9:
			cat_tit_num[0] = str(inc)
			hlf = cat_tit_num[0] + "." +cat_tit_num[1]
			inc=inc +1
			full = "https://"+cat_tit[2]+"/"+cat_tit[3]+"/"+cat_tit[4]+"/"+cat_tit[5]+"/"+cat_tit[6]+"/"+cat_tit[7]+"/"+hlf
			print(full)
			pl = Title1 + str(inc) + ".jpg"
			urllib.request.urlretrieve(full, pl)
			print("Added " + Title1 )
			#plt.ion()
			IMG = cv2.imread(pl,1)
			plt.imshow(IMG)
			plt.show(block = False)
			plt.pause(0.1)

		#cv2.destroyAllWindows()

loop_search()