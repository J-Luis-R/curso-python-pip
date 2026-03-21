import csv


def read_csv(path):
    with open(path, "r", encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        header = next(reader)
        # print(header) # imprime toda la primera fila del archivo
        data = []
        for row in reader:
            iterable = zip(header, row)
            country_dict = {key: value for key, value in iterable}
            # print(country_dict)
            data.append(country_dict)
            # print(list(iterable))
            # print("-" * 10)
            # print(row)
    return data


# if __name__ == "__main__":
#     data = read_csv("app\data.csv")
