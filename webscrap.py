import requests
from bs4 import BeautifulSoup
def find_meaning(word):
    response = requests.get(f"https://www.dictionary.com/browse/{word}")
    soup = BeautifulSoup(response.content, "html.parser")
    definition = soup.find(class_="one-click-content css-nnyc96 e1q3nk1v1").get_text()
    return definition
print(find_meaning(word=input('Enter te word: ')))

