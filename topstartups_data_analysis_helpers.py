'''
This file holds all the functions used in the computational essay to
analyze data.
'''

def filter_data_for_funds(industry, data):
    '''
    This function filters out topstartups.io data based on a specific industry
    and collects funding values.

    Args:
    industry: a string that represents the name of an industry tag to focus on.
    data: a dictionary that represents the data scraped from topstartups.io.

    Returns:
    A 1 column array that holds the total funding value for companies.
    '''
    # initialize array with industry name
    total_funding_values = [industry]

    funding_values = data.values()

    # loop through the dictionary values
    for value in funding_values:
        # check if the company is part of the industry
        industries = value[0]
        if industry in industries:
            multiply_factor = value[2][1][-1]   # this represents "M" or "B"

            if multiply_factor == 'M':
                total_funding_values.append(int(value[2][1][1:-1])*1000000)
            elif multiply_factor == 'B':
                total_funding_values.append(int(value[2][1][1:-1])*1000000000)

    return total_funding_values


def filter_by_series(industry, data):
    '''
    Separates a specific industry's funding data by series, up to Series E.

    Filters only a specific industry's data and finds each company's funding
    amounts. Then splits these funding amounts based on series/seed. Anything
    past Series E is not considered as there are too few datapoints to generate
    an accurate analysis.

    Args:
    industry: a string that represents the name of an industry tag to focus on.
    data: a dictionary that represents the data scraped from topstartups.io.

    Returns:
    A list of tuples. The first value of the tuple is the series type, and the
    second value is the funding amount.
    '''
    # this will be a dictionary storing funding within one series/seed round
    series_and_seed = {}

    # these store all the funding info
    seed = []
    series_a = []
    series_b = []
    series_c = []
    series_d = []
    series_e = []

    data_values = data.values()

    # loop through the dictionary values
    for value in data_values:
        # check if the company is part of the industry
        industries = value[0]
        if industry in industries:
            multiply_factor = value[2][1][-1]   # this represents "M" or "B"
            if multiply_factor == 'M':
                funding_value = int(value[2][1][1:-1])*1000000
            elif multiply_factor == 'B':
                funding_value = int(value[2][1][1:-1])*1000000000

            # sort the values by series into lists to be stored
            if value[2][0] == "Seed":
                seed.append(funding_value)
            elif value[2][0] == "Series A":
                series_a.append(funding_value)
            elif value[2][0] == "Series B":
                series_b.append(funding_value)
            elif value[2][0] == "Series C":
                series_c.append(funding_value)
            elif value[2][0] == "Series D":
                series_d.append(funding_value)
            elif value[2][0] == "Series E":
                series_e.append(funding_value)

    # store the separated funding data
    series_and_seed["Seed"] = seed
    series_and_seed["Series A"] = series_a
    series_and_seed["Series B"] = series_b
    series_and_seed["Series C"] = series_c
    series_and_seed["Series D"] = series_d
    series_and_seed["Series E"] = series_e

    return series_and_seed


def find_num_employees(industry, data):
    '''
    Finds all the number of employees for companies in a specific industry.

    Because topstartups.io has the number of employees as a range of values
    (ex: `11-50 employees`), the higher value as an integer will be used so it
    is easier to work with.

    Args:
    industry: a string that represents the name of an industry tag to focus on.
    data: a dictionary that represents the data scraped from topstartups.io.

    Returns:
    An array of integers that represent the number of employees each company
    has within a specific industry.
    '''
    number_employees = []

    data_values = data.values()

    # loop through the dictionary values
    for value in data_values:
        # check if the company is part of the industry
        if industry in value[0]:
            if '+' in value[1]:
                number_employees.append(value[1].split('+')[0])
            else:
                number_employees.append(value[1].split('-')[1].split(' ')[0])

    return number_employees


def find_funding_values(industry, data):
    '''
    Finds the funding values for companies in a specific industry.

    Args:
    industry: a string that represents the name of an industry tag to focus on.
    data: a dictionary that represents the data scraped from topstartups.io.

    Returns:
    An array of integers that represent the funding value each company has
    obtained within a specific industry.
    '''
    funding_values = []

    data_values = data.values()

    # loop through the dictionary values
    for value in data_values:
        # check if the company is part of the industry
        if industry in value[0]:
            multiply_factor = value[2][1][-1]   # this represents "M" or "B"
            if multiply_factor == 'M':
                funding_value = int(value[2][1][1:-1])*1000000
            elif multiply_factor == 'B':
                funding_value = int(value[2][1][1:-1])*1000000000
            funding_values.append(funding_value)

    return funding_values
