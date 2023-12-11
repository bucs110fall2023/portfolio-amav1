import requests
import urllib.parse


class MealAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://www.themealdb.com/api/json/v1/1/filter.php?i="

    def search_by_ingredient(self, ingredient):
        try:
            encoded_ingredient = urllib.parse.quote_plus(ingredient)
            url = self.base_url + encoded_ingredient
            response = requests.get(url)  # Removed MealAPI=MealAPI from here
            response.raise_for_status()
            data = response.json()
            return data.get('meals') if 'meals' in data else None
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            return None

def validate_ingredient(ingredient):
    return ingredient is not None and len(ingredient.strip()) > 0
