import requests
from bs4 import BeautifulSoup
import pandas as pd



# Verilerin alınacağı web sitesi
url = input("Please Enter url: ")

# İstek gönder ve web sitesindeki HTML kodunu al
response = requests.get(url)
html_content = response.content

# HTML kodunu BeautifulSoup kullanarak analiz et
soup = BeautifulSoup(html_content, 'html.parser')

# Örneğin, web sitesindeki tüm h1 etiketlerini çıkarabiliriz
headers = []
for header in soup.find_all('strong'):
    headers.append(header.text.strip())

# headers listesini bir Pandas DataFrame'ine dönüştürelim
df = pd.DataFrame(headers, columns=['Başlıklar'])

# DataFrame'imizi ekrana yazdıralım
print(df)
