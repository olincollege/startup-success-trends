# Startup Data Web Scraper from topstartups.io

This project is made for web scraping of all the startups in topstartups.io. It gets the URL of a webpage which (in this case is topstartups.io) and a list of 1,212 startups companies that we want to scrape. This data can be either text or any HTML tag value of that page. Then the web scraper filters out company names, industries it is a part of, funding values from the latest series round, and the number of employees. All of this data is written to a json file to be used for compiling graphs about the scraped data.

## How to use:

You can either use the webscraper file alone to scrape data, or you could use the whole repo as a kind of framework to build your own personal webscraper upon. The latter will require modifying the code.

### Features

1. Scrape multiple pages
2. Store scraped data as JSON for easy parsing

This project is compatible with python 3.

## Installations

Install the latest version from the git repository using pip:

`$ pip install git+https://github.com/alirezamika/autoscraper.git`

This project implements two packages to that require a local download: BeautifulSoup and matlibplot.

Install BeautifulSoup:

`$ pip install beautifulsoup4`

Install matlibplot:

`$ pip install matplotlib`
