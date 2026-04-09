from charts import generate_bar_chart, generate_pie_chart
from read_csv import read_csv
from utils import get_by_continent, population_by_country, get_population
import pandas as pd

def run():
    
    """
    data = list(filter(lambda item: item['Continent'] == 'South America', data)) 
    countries = list(map(lambda x: x['Country'], data))
    percentages = list(map(lambda x: x['World Population Percentage'], data))
    """
    
    # data = read_csv("data.csv")
    
    df = pd.read_csv("data.csv")
    # print(df)
    # print("-"*80)
    df = df[df['Continent'] == 'South America']
    # print(df)
    
    countries = df['Country'].values
    percentages = df['World Population Percentage']
    generate_pie_chart(countries, percentages)
    
    
    data = read_csv("data.csv")
    ciudad = input("Ciudad: ")
    result = population_by_country(data, ciudad)
    

    if len(result) > 0:
        country = result[0]
        labels, values = get_population(country)
        generate_bar_chart(ciudad, labels, values)

    # countries, percentage = get_by_continent(data)
    # generate_pie_chart(countries, percentage)


if __name__ == "__main__":
    run()
