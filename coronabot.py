from bs4 import BeautifulSoup as  bs
import requests
from time import sleep


r = requests.get('https://www.worldometers.info/coronavirus/')
soup = bs(r.text, 'html.parser')


def findall():
    for num in soup.select('.maincounter-number'):
        numbers = num.select('.maincounter-number >span')
        print(numbers[0].text)
findall()