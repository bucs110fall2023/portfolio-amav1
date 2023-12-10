from flask import Flask, jsonify, request, render_template
import requests

app = Flask(__name__, template_folder='templates')

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
