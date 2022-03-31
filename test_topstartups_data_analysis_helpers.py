'''
This file holds all the unit tests for the file
`topstartups_data_analysis_helpers.py`.
'''
import topstartups_data_analysis_helpers as helper_file


def test_filter_data_for_funds():
    '''
    Check the case where there are 0 industry matches.
    '''
    assert helper_file.filter_data_for_funds("SaaS", 
        {"Ramp": [["FinTech", "Enterprise Software"], "201-500 employees",
            ["Series D", "$750M"]],
        "FRVR": [["Mobile", "Games"], "51-100 employees",
            ["Series A", "$76M"]]}
        ) == ["SaaS"]


def test_filter_by_series():
    '''
    Check the case where some of the dictionary is empty.
    '''
    assert helper_file.filter_by_series("FinTech",
        {"Pogo": [["Consumer", "Mobile App", "FinTech"], "11-50 employees",
            ["Seed", "$15M"]]}
        ) == {"Seed": [15000000], "Series A": [], "Series B": [], "Series C": [],
            "Series D": [], "Series E": []}


def test_find_num_employees():
    '''
    Check the case where the employees is displayed as `5000+`.
    '''
    assert helper_file.find_num_employees("Delivery",
        {"Getir": [["Delivery", "Grocery", "Consumer"], "5000+ employees",
            ["Series E", "$768M"]]}
        ) == ['5000']


def test_find_funding_values():
    '''
    Check the case where funding is over 1 billion.
    '''
    assert helper_file.find_funding_values("SaaS",
        {"Celonis": [["Analytics", "Business Intelligence", "SaaS",
            "Enterprise Software"], "1001-5000 employees",
            ["Series D", "$1B"]]}
        ) == [1000000000]
