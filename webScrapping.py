# In this code I went into the link, then all the dates and titles were found then Zip helped 
# me to join them and print them lastly the same thing was done for thoes conferences which were
# conducted in London and they were printed in two different ways
#-----------------------------------------------------------------------------------------------------------

import requests
import re
from bs4 import BeautifulSoup


res=requests.get("https://conferenceindex.org/conferences/programming-languages")

if res.status_code == 200:

    dates=[]
    titles=[]
    londonDates=[]
    londonTitles=[]
    soup=BeautifulSoup(res.content,"html.parser")
    lis=soup.select("ul.list-unstyled>li")
    for li in lis:
        text=li.text.strip()
        date=re.findall(r"[a-zA-Z]{3}\s\d\d",text)
        title=re.findall(r"[a-zA-Z]{3}\s\d\d\s*(.+)",text)
        londonDate=re.findall(r"([a-zA-Z]{3}\s\d\d)\s*.+\s*-\sLondon,\sUnited\sKingdom",text)
        londonTitle=re.findall(r"[a-zA-Z]{3}\s\d\d\s*(.+)\s*-\sLondon,\sUnited\sKingdom",text)
        dates.extend(date)
        titles.extend(title)
        londonDates.extend(londonDate)
        londonTitles.extend(londonTitle)

else:
    print("Error: ",res.status_code)


#---------------------------------------------------------------------------------------------------------
# Running code:
#---------------------------------------------------------------------------------------------------------

##First procedure(All conferences)
# conferences= "\n".join("Date: '{}'\tTopic: '{}'".format(x,y) for x,y in zip(dates,titles))
# print("Conferences will be conducted:\n")
# print(conferences)


##Second procedure(London conferences)
# print("Conferences will be conducted in London:\n")
# for x,y in zip(londonDates,londonTitles):
#     print(f"Date: '{x}'\tTopic: '{y}'")


##Third procedure(London conferences)
# print("Conferences will be conducted in London:\n")
# for item in range(len(londonDates)):
#     print(f"Date: '{londonDates[item]}' \tTopic: '{londonTitles[item]}'")


