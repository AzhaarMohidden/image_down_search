import numpy as np
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as Img
from bs4 import BeautifulSoup as soup
import urllib.request
import random
my_url = 'file:///home/azhaar/Desktop/test_web/Sci-Fi%20HUD%20-%20Gnome-look.org.html'
containers_t="sdf"

uClient = urllib.request.urlopen(my_url)
page_html =uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")

containers = page_soup.findAll("img",{"class":"logo"})
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
		Title = containers[0]["src"]
		while True:
			urllib.request.urlretrieve(Title, "1.jpg")
			print("Added " + Title )
			#plt.ion()
		#cv2.destroyAllWindows()

loop_search()