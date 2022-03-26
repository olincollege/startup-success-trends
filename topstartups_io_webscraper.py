from ast import Num
import numbers
from bs4 import BeautifulSoup
import requests


def find_data_for_an_industry(industry):
    '''
    Scrapes the website topstartups.io for company data for a specific industry.

    Specifically, the name of the company, industry type, and seed/series funding
    are recorded.
    '''

    html_text = requests.get('https://topstartups.io').text
    soup = BeautifulSoup(html_text, 'lxml')
    text_boxes = soup.find_all('div', id = 'item-card')


    file = open("topstartups_data.txt", "w")
    for text_box in text_boxes:
        title = text_box.find('a', id = 'startup-website-link').text
        
        industry_tag = text_box.find_all('span', id = 'industry-tags')
        industry_tags = []
        for tag in industry_tag:
            tag_as_string = str(tag.text)
            if len(tag_as_string) == 0:
                continue
            elif tag_as_string[0] == " ":
                tag_as_string = tag_as_string[1:]
            industry_tags.append(tag_as_string)

        funding_amount = text_box.find_all('span', id = 'funding-tags')
        funding_by_series = []
        for amount in funding_amount:
            amount_as_string = str(amount.text)
            if len(amount_as_string) == 0:
                continue
            elif amount_as_string[0] == " ":
                amount_as_string = amount_as_string[1:]
            
            # filter amounts by seeds/series here
            if "Series" in amount_as_string:
                series_index = amount_as_string.index("Series")
                series_type = amount_as_string[series_index : series_index+8]
                series_value = amount_as_string.split(" ", 1)[0]
                funding_by_series.append((series_type, series_value))
            elif "Seed" in amount_as_string:
                series_value = amount_as_string.split(" ", 1)[0]
                funding_by_series.append(("Seed", series_value))

        # overwrite the contents of the file with the new data
        if industry in industry_tags:
            file.write(f"Company Name: {title}\n")
            file.write(f"Industry Type: {industry_tags}\n")
            file.write(f"Funding by series: {funding_by_series}\n")
    file.close()
