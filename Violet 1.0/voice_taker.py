import re
from urllib.request import urlopen

from bs4 import BeautifulSoup
from lxml import html, etree
import requests


# url = 'https://valorant.fandom.com/ru/wiki/Jett/Фразы' #https://valorant.fandom.com/ru/wiki/Jett/%D0%A4%D1%80%D0%B0%D0%B7%D1%8B
#
# s = requests.Session()
#
# headers = {
# 'User-Agent' : 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36'
#     }
#
# r = requests.get(url, headers = headers)
# #
# html_text = r.text
# print(html_text)

#
# with open('test.html', 'w', encoding='utf-8') as output_file:
#   output_file.write(r.text)
#
# #
# # read local html file and set up lxml html parser
# local = 'http://localhost:63342'
# with urlopen(local) as response:
#   #html_response = response.read()
#

with open('test.html', 'r', encoding='utf-8') as output_file:
  html_text = output_file.read()

# htmlparser = etree.HTMLParser()
# tree = etree.fromstring(html_text, htmlparser)
#
#
# for i in range(4):
#     print(etree.tostring(tree.xpath('//ul/li/div[@class ="audio-button"]/audio[@src]')[i]))
# #https://static.wikia.nocookie.net/valorant/images/b/b6/RU_Wushu_PickMe.ogg/revision/latest?cb=20230301143549&path-prefix=ru
# #https://static.wikia.nocookie.net/valorant/images/b/b6/RU_Wushu_PickMe.ogg/revision/latest?cb=20230301143549&amp;path-prefix=ru

soup = BeautifulSoup(html_text, 'html.parser')

list_li = soup.findAll('div', class_ = 'audio-button')
ready = dict()
index = 0
for item in list_li:
  try:
    name = item.findParent().text
    name = re.split('\s', name, 3)[3]
    name = name[1:]
    if 'Эй, Phoenix! Если умрёшь, чур я заберу твою куртку.' in name:
      name = 'Эй, Phoenix! Если умрёшь, чур я заберу твою куртку.'
    elif 'Skye, а ты не думала призывать других зверей7' in name:
      name = 'Skye, а ты не думала призывать других зверей7 Львов, например, или… О! Драконов!'
    elif 'Я пыталась. Но получилось… не очень.' in name :
      name = 'Проложи нам путь, Skye. Я тебя прикрою.'
    if name[-1] != '.':
      name += '.'
    name = re.sub('\?', '7', name)
    print(name)
    ready_item = item.find('audio').get('src')
    print(ready_item)
    print()
    ready[name] = ready_item

  except AttributeError:
    print('End')


print(len(ready))

for i in range(len(ready)):
  local = list(ready.values())[i]
  with urlopen(local) as response:
    file = response.read()
    with open(list(ready.keys())[i] + 'mp3', 'wb') as output_file:
      output_file.write(file)


list_links = list_li.find('audio').get('src')
print(list_links)

