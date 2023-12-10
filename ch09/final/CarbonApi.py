import requests
from flask import Flask, jsonify, request

app = Flask(__name__)

class MealAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = 'https://www.themealdb.com/api/json/v1/' + self.api_key + '/search.php?s='

    def search_meal(self, meal_name):
        try:
            url = self.base_url + meal_name
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            meals = data.get('meals')
            return meals if meals else None
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            return None

@app.route('/')
def index():
    return "Welcome to the Meal API"

@app.route('/search_meal', methods=['GET'])
def search_meal():
    meal_name = request.args.get('meal_name')
    api_key = '1' 

    if meal_name:
        meal_instance = MealAPI(api_key)
        results = meal_instance.search_meal(meal_name)
        if results:
            return jsonify({"results": results})
        else:
            return jsonify({"message": "No results found."}), 404
    else:
        return jsonify({"message": "Invalid or missing meal name."}), 400

if __name__ == '__main__':
    app.run(debug=True)
