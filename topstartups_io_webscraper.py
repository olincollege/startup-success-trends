'''
Scrapes the website topstartups.io for company data.

Specifically, the name of the company, industry type, and seed/series funding
are recorded. After the data is acquired, it is stored into a text file for
further analysis.
'''

import json
from bs4 import BeautifulSoup
import requests


URL = "https://topstartups.io/?page="

company_data = {}

# iterate through all the pages of the website
for page in range(1, 68):
    # get the html text for the entire page
    html_text = requests.get(URL + str(page)).text
    soup = BeautifulSoup(html_text, 'lxml')

    # within the html, find all instances of `div` items with id `item-card`
    text_boxes = soup.find_all('div', id = 'item-card')

    # find all the company data and store in a dictionary with
    # company name as the key and info as a tuple
    for text_box in text_boxes:
        # get the name of the company
        company_name = text_box.find('a', id = 'startup-website-link').text

        # get the industry tags of the company
        industry_tag = text_box.find_all('span', id = 'industry-tags')
        industry_tags = []
        for tag in industry_tag:
            tag_as_string = str(tag.text)
            if len(tag_as_string) == 0:
                continue
            if tag_as_string[0] == " ":
                tag_as_string = tag_as_string[1:]
            industry_tags.append(tag_as_string)

        # get the number of employees
        number_employees = text_box.find('span', id = 'company-size-tags').text

        # get the seed and/or series funding values
        funding_amount = text_box.find_all('span', id = 'funding-tags')

        for amount in funding_amount:
            amount_as_string = str(amount.text)
            if len(amount_as_string) == 0:
                continue
            if amount_as_string[0] == " ":
                amount_as_string = amount_as_string[1:]

            # filter amounts by seeds/series here
            if "Series" in amount_as_string:
                series_index = amount_as_string.index("Series")
                series_type = amount_as_string[series_index : series_index+8]
                series_value = amount_as_string.split(" ", 1)[0]
                funding_by_series = (series_type, series_value)
            elif "Seed" in amount_as_string:
                series_value = amount_as_string.split(" ", 1)[0]
                funding_by_series = ("Seed", series_value)

        # store everything in the `company_data` dictionary
        company_data[company_name] = (industry_tags, number_employees, funding_by_series)



# write data to the file `topstartups_data.json`
with open('topstartups_data.json', 'w') as file:
    json.dump(company_data, file)
file.close()
