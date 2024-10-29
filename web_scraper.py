import requests
from bs4 import BeautifulSoup
url="<url>"
try:
    response=requests.get(url)
    response.raise_for_status()
    soup=BeautifulSoup(response.content,"html.parser")
    text=soup.get_text()
    file_path="Webpage.txt"
    with open (file_path,"w",encoding="utf-8") as file:
        file.write(text)
    print(f"Webpage content has been successfully saved into {file_path}")
except requests.exceptions.RequestException as e:
    print(f"Error fetching the url:{e}")