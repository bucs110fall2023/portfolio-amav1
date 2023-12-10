from flask import Flask, jsonify, request, render_template
import requests

app = Flask(__name__, template_folder='templates')

class MealAPI: 
    def __init__(self, url):
        self.api_url = url
    
    def get(self):
        try:
            response = requests.get(self.api_url)
            response.raise_for_status()
            data = response.json()
            return data  
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            return None

def validate_url(url):
    return url.startswith("http://") or url.startswith("https://")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_meal_results', methods=['GET'])
def get_meal_results():
    user_url = request.args.get('url')

    if not user_url or not validate_url(user_url):
        return jsonify({"message": "Invalid or missing URL."}), 400
    
    meal_instance = MealAPI(user_url)
    results = meal_instance.get()
    
    if results is not None:
        return jsonify({"results": results})
    else:
        return jsonify({"message": "No results found."}), 404

if __name__ == '__main__':
    app.run(debug=True)
