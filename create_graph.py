import matplotlib.pyplot as plt
from datetime import datetime


def create_country_covid_graph(data):
    
    xAxis = [key for key, value in data.items()]
    yAxis = [value for key, value in data.items()]
    plt.grid(True)

    fig = plt.figure()
    plt.xlabel('Country')
    plt.ylabel('Total Covid-19 cases per 1M population')

    plt.bar(xAxis,yAxis, color='violet')

    #Add a time stamp
    now = datetime.now()
    timestamp = now.strftime("%d-%m-%Y_%H:%M:%S")

    filepath = f"covid_graph_images/Country_specific_total_covid_cases_per_1M_population/{timestamp}.png"

    plt.savefig(filepath)

    return filepath

def create_indian_cities_covidcases_graph(data):
    xAxis = [key for key, value in data.items()]
    yAxis = [value for key, value in data.items()]
    plt.grid(True)

    fig = plt.figure()
    plt.bar(xAxis,yAxis, color='red')
    plt.xlabel('Indian Cities')
    plt.ylabel('Total Confirmed Covid-19 cases')

    #Add timestamp
    now = datetime.now()
    timestamp = now.strftime("%d-%m-%Y_%H:%M:%S")

    filepath = f"covid_graph_images/Indian_city_specific_total_confirmed_cases/{timestamp}.png"

    plt.savefig(filepath)

    return filepath


def create_indian_cities_covid_change_graph(data):
    xAxis = [key for key, value in data.items()]
    yAxis = [value for key, value in data.items()]
    plt.grid(True)

    fig = plt.figure()
    plt.bar(xAxis,yAxis, color='purple')
    plt.xlabel('Indian cities')
    plt.ylabel('Daily change in Covid-19 cases')

    #Add timestamp
    now = datetime.now()
    timestamp = now.strftime("%d-%m-%Y_%H:%M:%S")
    filepath = f"covid_graph_images/Indian_city_specific_daily_change_in_cases/{timestamp}.png"

    plt.savefig(filepath)

    return filepath

