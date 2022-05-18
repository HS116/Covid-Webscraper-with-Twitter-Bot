import matplotlib.pyplot as plt

def create_country_covid_graph(data):
    
    xAxis = [key for key, value in data.items()]
    yAxis = [value for key, value in data.items()]
    plt.grid(True)

    fig = plt.figure()
    plt.xlabel('Country')
    plt.ylabel('Total Covid-19 cases per 1M population')

    plt.bar(xAxis,yAxis, color='violet')

    plt.show()

def create_indian_cities_covidcases_graph(data):
    xAxis = [key for key, value in data.items()]
    yAxis = [value for key, value in data.items()]
    plt.grid(True)

    fig = plt.figure()
    plt.bar(xAxis,yAxis, color='red')
    plt.xlabel('Indian Cities')
    plt.ylabel('Total Confirmed Covid-19 cases')

    plt.show()

def create_indian_cities_covid_change_graph(data):
    xAxis = [key for key, value in data.items()]
    yAxis = [value for key, value in data.items()]
    plt.grid(True)

    fig = plt.figure()
    plt.bar(xAxis,yAxis, color='purple')
    plt.xlabel('Indian cities')
    plt.ylabel('Daily change in Covid-19 cases')

    plt.show()
