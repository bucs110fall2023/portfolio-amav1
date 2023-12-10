import requests

class MealAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = f'https://www.themealdb.com/api/json/v1/{self.api_key}/filter.php?i='

    def search_by_ingredient(self, ingredient):
        try:
            url = self.base_url + ingredient
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            return data.get('meals') if 'meals' in data else None
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            return None

def validate_ingredient(ingredient):
    return ingredient is not None and len(ingredient.strip()) > 0
