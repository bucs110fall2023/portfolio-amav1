from flask import Flask, jsonify, request

app = Flask(__name__)

class CarbonAPI:
    def __init__(self, url):
        self.api_url = 'https://api.websitecarbon.com' + url
    
    def get(self):
        try:
            response = request.get(self.api_url)
            response.raise_for_status()
            data = response.json()
            results = data.get('results')
            return results if results else None
        except request.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            return None

@app.route('/')
def index():
    return "Welcome to the Carbon API"

@app.route('/get_carbon_results', methods=['GET'])
def get_carbon_results():
    user_url = request.args.get('url')

    if user_url:
        carbon_instance = CarbonAPI(user_url)
        results = carbon_instance.get()
        if results:
            return jsonify({"results": results})
        else:
            return jsonify({"message": "No results found."}), 404
    else:
        return jsonify({"message": "Invalid or missing URL."}), 400

if __name__ == '__main__':
    app.run(debug=True)
