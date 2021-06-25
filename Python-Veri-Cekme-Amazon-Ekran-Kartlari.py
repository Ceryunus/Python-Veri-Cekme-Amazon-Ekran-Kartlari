import requests
from bs4 import BeautifulSoup

ULR = "https://www.amazon.com.tr/s?k=ekran+kartı&__mk_tr_TR=ÅMÅŽÕÑ&ref=nb_sb_noss_1"
header = {
    "User-Agent": "USER AGENTİNİZİ BURAYA GİRECEKSİNİZ YOKSA AMAZON SİZİ BOT ZANLEDEREK VERİ CEKMEYİ ENGELLİYEBİLİYOR"}
r = requests.get(ULR, headers=header)
soup = BeautifulSoup(r.content, "lxml")
items = soup.find_all("div",
                      attrs={"class": 'sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col sg-col-4-of-20'})

itemList = []
itemDict = {}
for item in items:
    itemsLink = item.find_all("div", attrs={"class": "a-section a-spacing-medium"})

    for i in itemsLink:
        link = i.find("span", attrs={"class": "rush-component"})
        startLink = "https://www.amazon.com.tr"
        try:
            endLink = link.a.get("href")
            lastLink = startLink + endLink
            print(lastLink)

            itemgo = requests.get(lastLink, headers=header)
            print(itemgo.content)
            soup2 = BeautifulSoup(itemgo.content, "lxml")
            AllItemContent = soup2.find_all("div", attrs={
                "class": "a-expander-content a-expander-section-content a-section-expander-inner"})
            for technic in AllItemContent:
                trler = technic.find_all("tr")
                print(trler)
                for i in trler:
                    print(i)
                    keys = i.find("th", attrs={"prodDetSectionEntry"}).string.replace("\n", "")
                    print(keys)
                    values = i.find("td", attrs={"prodDetAttrValue"}).string.replace("\n", "")
                    itemDict[keys] = values


                itemsappendlistparam = itemDict.copy()
                itemList.append(itemsappendlistparam)
                itemDict.clear()
                print("ok")
        except:
            print("!!!!!!!!!!VERI CEKILEMEDI!!!!!!!!!!")
        # trler=AllItemContent.find_all("tr")
        # print(trler)

print(itemList)
neyeGore = []
for i in range(len(itemList)):
    for k, v in itemList[i].items():
        if k not in neyeGore:
            neyeGore.append(k)
        # if k==filterForitems:
        #     print(k,v)

print(neyeGore)
filterForitems = input("Neye Göre Listelesin : ")

for i in range(len(itemList)):
    print(itemList[i],
          end="\n------------------------------------------------------------------------\n")
    for k, v in itemList[i].items():
        if k == filterForitems:
            print(k, v)
