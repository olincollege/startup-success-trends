'''
This file holds all the unit tests for the file
`topstartups_data_analysis_helpers.py`.
'''
from abc import get_cache_token
import topstartups_data_analysis_helpers as helper_file
import pytest

FILTER_DATA_CASES = [
    # zero instances
    ("SaaS", {"Ramp": [["FinTech", "Enterprise Software"], "201-500 employees",
            ["Series D", "$750M"]],
        "FRVR": [["Mobile", "Games"], "51-100 employees",
            ["Series A", "$76M"]]},
            ["SaaS"]),
    # one instance
    ("SaaS", {"Ramp": [["FinTech", "Enterprise Software"], "201-500 employees",
            ["Series D", "$750M"]],
        "FRVR": [["Mobile", "Games"], "51-100 employees",
            ["Series A", "$76M"]],
        "Modern Animal": [["Consumer", "SaaS", "Pets", "Health"],
            "51-100 employees", ["Series B", "$36M"]]},
            ["SaaS", 36000000]),
    # two instances
    ("Enterprise Software", {"ClickUp": [["SaaS", "Enterprise Software",
            "Productivity Tools"], "501-1000 employees", ["Series C", "$400M"]],
        "Truepill": [["Health Care", "Pharmaceuticals"], "201-500 employees",
            ["Series D", "$142M"]],
        "Devo": [["Security", "Enterprise Software"], "501-1000 employees",
            ["Series E", "$250M"]],
        "Vendease": [["Marketplaces", "Resaurants", "Food And Drinks"],
            "51-100 employees", ["Seed", "$3M"]],
        "copy.ai": [["SaaS", "Artificial Intelligence"], "11-50 employees",
            ["Series A", "$11M"]],
        "Foodology": [["Food Delivery", "Restaurants"], "51-100 employees",
            ["Series A", "$15M"]],
        "Lokal": [["Consumer", "Apps", "Social Media"], "101-200 employees",
            ["Series A", "$12M"]]},
            ["Enterprise Software", 400000000, 250000000])
]


FILTER_BY_SERIES_CASES = [
    # only one of the funding rounds is filled
    ("FinTech",
        {"Pogo": [["Consumer", "Mobile App", "FinTech"], "11-50 employees",
            ["Seed", "$15M"]]},
        {"Seed": [15000000], "Series A": [], "Series B": [],
        "Series C": [], "Series D": [], "Series E": []}),
    # multiple funding rounds are filled
    ("SaaS",
        {"ClickUp": [["SaaS", "Enterprise Software", "Productivity Tools"],
            "501-1000 employees", ["Series C", "$400M"]],
        "Matik": [["SaaS", "Sales", "Enterprise Software"], "11-50 employees",
            ["Series A", "$20M"]], "Sprinter Health": [["Health Care",
            "Medical", "Consumer"], "11-50 employees", ["Series A", "$33M"]],
        "Gem": [["Recruiting", "Enterprise Software", "SaaS"],
            "201-500 employees", ["Series C", "$37M"]],
        "Clio": [["SaaS", "Legal Tech"], "501-1000 employees",
            ["Series E", "$20M"]]},
        {"Seed": [], "Series A": [20000000], "Series B": [],
        "Series C": [400000000, 37000000], "Series D": [],
        "Series E": [20000000]}),
    # series past Series E shouldn't fill any boxes
    ("SaaS",
        {"Carta": [["FinTech", "Equity", "Enterprise Software", "SaaS"],
            "1001-5000 employees", ["Series G", "$80M"]]},
        {"Seed": [], "Series A": [], "Series B": [],
        "Series C": [], "Series D": [], "Series E": []}),
]

NUM_EMPLOYEES_CASES = [
    # where employees is displayed as `5000+`
    ("Delivery",
        {"Getir": [["Delivery", "Grocery", "Consumer"], "5000+ employees",
            ["Series E", "$768M"]]},
        ['5000']),
    # where employees is displayed as a range `1-10`
    ("Insurance",
        {"Shepherd": [["FinTech", "Insurance", "Construction"],
            "1-10 employees", ["Seed", "$6M"]]},
        ['10']),
    # multiple companies are stored correctly
    ("Insurance",
        {"Shepherd": [["FinTech", "Insurance", "Construction"],
            "1-10 employees", ["Seed", "$6M"]],
        "SafetyWing": [["Consumer", "Freelancers", "Insurance"],
            "51-100 employees", ["Series A", "$12M"]]},
        ['10', '100'])
]


FUNDING_VALUES_CASES = [
    # where funding is over 1 billion.
    ("SaaS",
        {"Celonis": [["Analytics", "Business Intelligence", "SaaS",
            "Enterprise Software"], "1001-5000 employees",
            ["Series D", "$1B"]]},
        [1000000000]),
    # where multiple funding values are either million of billion.
    ("SaaS",
        {"Celonis": [["Analytics", "Business Intelligence", "SaaS",
            "Enterprise Software"], "1001-5000 employees",
            ["Series D", "$1B"]],
        "Hex": [["Analytics", "Big Data", "SaaS"], "11-50 employees",
            ["Series B", "$52M"]]},
        [1000000000, 52000000])
]


@pytest.mark.parametrize("industry, data, expected_value", FILTER_DATA_CASES)
def test_filter_data_for_funds(industry, data, expected_value):
    '''
    Check the cases where there are 0, 1, or 2 industry matches.
    '''
    assert helper_file.filter_data_for_funds(industry,
        data) == expected_value


@pytest.mark.parametrize("industry, data, expected_value", FILTER_BY_SERIES_CASES)
def test_filter_by_series(industry, data, expected_value):
    '''
    Check cases where the returned values have none or some values.
    '''
    assert helper_file.filter_by_series(industry, data) == expected_value


@pytest.mark.parametrize("industry, data, expected_value", NUM_EMPLOYEES_CASES)
def test_find_num_employees(industry, data, expected_value):
    '''
    Check cases for employees.
    '''
    assert helper_file.find_num_employees(industry, data) == expected_value


@pytest.mark.parametrize("industry, data, expected_value", FUNDING_VALUES_CASES)
def test_find_funding_values(industry, data, expected_value):
    '''
    Check cases for funding values.
    '''
    assert helper_file.find_funding_values(industry, data) == expected_value
