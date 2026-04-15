import requests

def get_categories():
    r = requests.get('https://api.escuelajs.co/api/v1/categories')
    print(r.status_code)
    print("-"*40)
    print(r.text)
    print("-"*40)
    print(type(r.text))
    print("-"*40)
    categories = r.json()
    for category in categories:
        print(category['name'])
        print("-"*40)