from charts import generate_bar_chart, generate_pie_chart
from read_csv import read_csv
from utils import get_by_continent, population_by_country, get_population


def run():
    data = read_csv("data.csv")
    ciudad = input("Ciudad: ")
    result = population_by_country(data, ciudad)

    if len(result) > 0:
        country = result[0]
        labels, values = get_population(country)
        generate_bar_chart(ciudad, labels, values)

    countries, percentage = get_by_continent(data)
    generate_pie_chart(countries, percentage)


if __name__ == "__main__":
    run()
