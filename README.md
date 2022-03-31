# Startup Data Web Scraper from topstartups.io

This project is made for web scraping of all the startups in topstartups.io. It gets the URL of a webpage which (in this case is topstartups.io) and a list of 1,212 startups companies that we want to scrape. This data can be either text or any HTML tag value of that page. Then the web scraper filters out company names, industries it is a part of, funding values from the latest series round, and the number of employees. All of this data is written to a json file to be used for compiling graphs about the scraped data.

## Installations

This project is compatible with python 3.
Install the latest version from the git repository using pip:
`$ pip install git+https://github.com/alirezamika/autoscraper.git`

This project implements two packages to that require a local download: BeautifulSoup and matlibplot.
Install BeautifulSoup:
`$ pip install beautifulsoup4`
How to use:
https://beautiful-soup-4.readthedocs.io/en/latest/

install matlibplot:
`$ pip install matplotlib`
How to use:
https://matplotlib.org/3.5.1/tutorials/introductory/pyplot.html
