import requests
from bs4 import BeautifulSoup

response=requests.get("https://www.magicbricks.com/property-for-rent/residential-real-estate?proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment,Service-Apartment,Residential-House,Villa&cityName=Mumbai")

print(response.content)

print(response.status_code)

soup= BeautifulSoup(response.content,"html.parser")

print(soup)

print(soup.prettify())


find('a')


find_all('a')

find_all("img")


find_all("div")

find_next_sibilings("a")





card= soup.find_all("div",attrs={"class":"flex relative clearfix m-srp-card__container"})

print(card)

for card in cards:

price=card.find_all("div",attrs={"class":"m-srp-card__info flex__item"})


print(price.txt)


title=card.find_all("span",attrs={"class":"m-srp-card__title__bhk"})

print(title.txt.strip("\n"))

carpet_area=card.find("div",attrs={"class":"m-srp-card__summary__info"}\

print(carpet_area.txt)


data="{} {} {}".format(title.txt.strip("\n",price.txt,carpet_area.txt)

print(data)









