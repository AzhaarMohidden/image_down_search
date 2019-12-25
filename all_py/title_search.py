from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

#my_url = 'https://vk.com/video?notsafe=1&q=anal'

containers = "sdf"

def analize():
    global containers
    my_url = 'https://www.porntrex.com/categories/anal/'
    print("making containers ")
    uClient = uReq(my_url)
    page_html =uClient.read()
    uClient.close()
    page_soup = soup(page_html, "html.parser")
    print("Page parsing..")
    containers = page_soup.findAll("p",{"class":"inf"})


def loop_search(z):
    global containers
    print("Doing loop search")
    for x in range(len(containers)):
        m = str(z)
        Title = containers[x].a["title"]
        cat_tit = Title.split(" ")
        cat_num = len(cat_tit)
        for l in range(cat_num):
            #print(cat_tit[l])
            if cat_tit[l] == m:
                print(Title)
        print("-----------------------------------")

def all_titles():
    global containers
    print("Doing loop search")
    for x in range(len(containers)):
        Title1 = containers[x].a["title"]
        print(str(x)+". "+Title1)



#containers = page_soup.findAll("div", {"class":"video_item _video_item ge_video_item_"})
analize()
all_titles()
print("going to A loop")
term = input('Input search term : ')
n = str(term)
loop_search(n)




    #print(Title)
