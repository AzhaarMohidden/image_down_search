from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

#my_url = 'https://vk.com/video?notsafe=1&q=anal'
my_url = 'https://www.porntrex.com/categories/anal/'


uClient = uReq(my_url)
page_html =uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")

containers = page_soup.findAll("div",{"class":"video-list"})
#containers = page_soup.findAll("div", {"class":"video_item _video_item ge_video_item_"})

out_filename = "newegg.csv"
headers= "URL"
f = open(out_filename, "w")
f.write(headers)


for x in range(len(containers)):
    Img = containers[x].div.a.img["data-src"]
    Img_url= str(Img).strip().replace("//","")
    print(Img_url)
    f.write(Img_url+ "\n")

f.close()  # Close the file
