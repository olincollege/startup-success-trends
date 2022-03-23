from ast import Num
import numbers
from tkinter.ttk import Style
from bs4 import BeautifulSoup
import requests


#html_text = requests.get('https://www.greatcollections.com/hotlist.php?cmd=hotlist&date=2022-3-27&cat_id=25&cat_name=Silver-Eagles%27).text
#soup = BeautifulSoup(html_text, 'lxml')
#textbox = soup.find('tr', class = 'alt1')
#text = text_box.find('a', href = "https://www.greatcollections.com/Coin/1135536/1986-1-Silver-Eagle-NGC-MS-70%22).text
#print(text)

print('put some industry tag that you are interested in:')
filtered_industry_tag = input('>')
print(f'filtering out {filtered_industry_tag}')

html_text = requests.get('https://topstartups.io/%27).text
soup = BeautifulSoup(html_text, 'lxml')
text_boxes = soup.find_all('div', id = 'item-card')
for text_box in text_boxes:
    title = text_box.find('a', id = 'startup-website-link').text
    Industry_Tag = text_box.find_all('span', id = 'industry-tags')
    funding_amount = text_box.find_all('span', id = 'funding-tags')

    if filtered_industry_tag not in Industry_Tag:
        print(f'Company name: {title}')
        for tag in Industry_Tag:
            print("Industry Tag: " + tag.text.replace(' ', '', 1))
        for f_tag in funding_amount:
            print("funding Tag: " + f_tag.text) 
        print('')
