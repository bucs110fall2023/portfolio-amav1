from flask import Flask, jsonify, request, render_template
import requests

app = Flask(__name__, template_folder='templates')

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

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search_by_ingredient', methods=['GET'])
def search_by_ingredient():
    user_ingredient = request.args.get('ingredient')
    api_key = '1'  

    if not validate_ingredient(user_ingredient):
        return jsonify({"message": "Invalid or missing ingredient."}), 400
    
    meal_instance = MealAPI(api_key)
    results = meal_instance.search_by_ingredient(user_ingredient)
    
    if results is not None:
        return jsonify({"results": results})
    else:
        return jsonify({"message": "No results found for this ingredient."}), 404

def main():
    app.run(debug=True)

if __name__ == '__main__':
    main()
