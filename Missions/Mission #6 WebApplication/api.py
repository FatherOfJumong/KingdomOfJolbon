import requests
import json



#url_for_categories = 'https://api.chucknorris.io/jokes/categories'
#response_category = requests.get('url_for_categories')

def generate_joke(categ):
    categories = ["animal","career","celebrity","dev","explicit","fashion","food","history","money","movie","music",
                 "political","religion","science","sport","travel"]

    if categ in categories:
        category = categ
    url_for_jokes = f'https://api.chucknorris.io/jokes/random?category={category}'
    response_joke = requests.get(url_for_jokes)

    joke = json.loads(response_joke.content)['value']
    return joke

def give_categories():
    categories = ["animal","career","celebrity","dev","explicit","fashion","food","history","money","movie","music",
                 "political","religion","science","sport","travel"]
    return categories
