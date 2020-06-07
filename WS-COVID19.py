import pandas as pd
import requests
from bs4 import BeautifulSoup
url =('https://www.mohfw.gov.in/')
text = requests.get(url)
soup = BeautifulSoup(text.content,"html.parser")
s = soup.find_all('tr')
d = 0
for i in s:
  a = i.text
  b = a.replace('\n' , '      ') 
  print(b)
  print("------------------------------------------------------------------------")
  d += 1
  if (d == 36):
    break