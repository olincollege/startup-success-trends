from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.failory.com/startups/mobile-apps- \
    unicorns%27').text
soup = BeautifulSoup(html_text, 'lxml')
company_infos = soup.find_all('div', class__ = 'listicle-startup-collection- \
    item w-dyn-item')
company_info = []

file = open("topstartups_data.txt", "w")
for info in company_infos:
    name = info.find('h3', class__ = 'listicle-h3 content-h3').text
    file.write(name)

    info_box = info.find_all('li', class__ = 'listicle-list-item')
    info_boxes = []
    for box in info_box:
        box_as_string = str(box.text)
        info_boxes.append(box_as_string)

    company_info.append(info_boxes)
    file.write(info_boxes)

print(company_info)
file.close()
