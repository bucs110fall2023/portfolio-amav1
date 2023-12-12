from flask import Flask, jsonify, request, render_template
from MealAPI import MealAPI, validate_ingredient
from QuotesAPI import QuotesAPI
import json

app = Flask(__name__, template_folder='templates', static_folder='static')
quotes_api = QuotesAPI()  

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_meal_results', methods=['GET'])
def search_by_ingredient():
    user_ingredient = request.args.get('ingredient')
    api_key = '1'

    if not validate_ingredient(user_ingredient):
        return jsonify({"message": "Invalid or missing ingredient."}), 400

    meal_instance = MealAPI(api_key)
    results = meal_instance.search_by_ingredient(user_ingredient)

    if results is not None:
        quote = quotes_api.daily_inspiration()  
        
        
        response = {
            "results": results,
            "quote_of_the_day": quote
        }
        
        resp_json = json.dumps(response, sort_keys=True, indent=10)
        return f"{resp_json}<br><a href='/'>Return Home</a>"
    else:
        return jsonify({"message": "No results found for this ingredient."}), 404

def main():
    app.run(debug=True)

if __name__ == '__main__':
    main()
