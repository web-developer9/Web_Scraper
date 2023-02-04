from bs4 import BeautifulSoup
import requests

URL = 'https://www.flipkart.com/motorola-g72-polar-blue-128-gb/p/itmec1a028ad0f56?pid=MOBGEA3CTXXRVKET&lid=LSTMOBGEA3CTXXRVKETFSX8DE&marketplace=FLIPKART&store=tyy%2F4io&srno=b_1_14&otracker=hp_bannerads_1_2.bannerAdCard.BANNERADS_Moto%2BDays_78CQMBJM1V86&fm=organic&iid=e0c18600-c0b3-491b-86c5-e55f0b691ab2.MOBGEA3CTXXRVKET.SEARCH&ppt=hp&ppn=homepage&ssid=3dgshn6okg0000001674416423085'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"}

page = requests.get(URL, headers=headers)

soup1 = BeautifulSoup(page.content, 'html.parser')

title = soup1.find(attrs={'class': "B_NuCI"}).get_text()
rating = soup1.find(attrs={'class': '_3LWZlK'}).get_text()
review = soup1.find(attrs={'class': "_2wzgFH"}).get_text()

print(review)
print(title)
print(rating)
