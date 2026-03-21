import csv

from charts import generate_pie_chart


def read_csv(path):
    # Tu código aquí 👇
    with open(path, "r", encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        header = next(reader)
        # total = 0
        data = []
        for row in reader:
            iterable = zip(header, row)
            country_dic = {key: value for key, value in iterable}
            # print(country_dic) # Imprime: {'Rank': '36', 'CCA3': 'AFG', 'Country': 'Afghanistan', 'Capital': 'Kabul', 'Continent': 'Asia', '2022 Population': '41128771', '2020 Population': '38972230', '2015 Population':
            #'33753499', '2010 Population': '28189672', '2000 Population': '19542982', '1990 Population': '10694796', '1980 Population': '12486631', '1970 Population': '10752971', 'Area (km²)': '652230', 'Density (per km²)': '63.0587', 'Growth Rate': '1.0257', 'World Population Percentage': '0.52'}
            data.append(country_dic)
            # print(row) # Imprime: ['36', 'AFG', 'Afghanistan', 'Kabul', 'Asia', '41128771', '38972230', '33753499', '28189672', '19542982', '10694796', '12486631', '10752971', '652230', '63.0587', '1.0257', '0.52']
    return data
    #         total += int(row[0])
    # return total


def get_country(data):
    return [country["Country"] for country in data]


def get_percentage(data):
    return [float(dato_por["World Population Percentage"]) for dato_por in data]


def concat_datos(country, porcentaje):
    iterable = zip(country, porcentaje)
    data = []
    dato = {key: value for key, value in iterable}
    data.append(dato)
    return data


def population_by_continent(data):
    by_continent = {
        dato["Country"]: dato["World Population Percentage"]
        for dato in data
        if dato["Continent"] == "North America"
    }
    countries = by_continent.keys()
    percentage = by_continent.values()
    return countries, percentage


data = read_csv("app\data.csv")

countries, percentage = population_by_continent(data)

# countries = get_country(data)
# porcentajes = get_percentage(data)
# print(data)

""" iterable = concat_datos(countries, percentage)
print(iterable)

continent = population_by_continent(data)
print(continent) """

# print(iterable[0])

# print(data)
generate_pie_chart(countries, percentage)

# diccionario = reduce(lambda d, par: {**d, par[0]: par[1]}, iterable, {})
# print(diccionario)  # {'a': 1, 'b': 2, 'c': 3}
# print(data[0])
