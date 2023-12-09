from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

class CarbonAPI: 
    def __init__(self, url):
        self.api_url = url
    
    def get(self):
        try:
            response = requests.get(self.api_url)
            response.raise_for_status()
            data = response.json()
            results = data.get('results')
            if results:
                return results
            else:
                return None
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            return None

def validate_url(url):
    
    return True if url.startswith("http://") or url.startswith("https://") else False

@app.route('/get_carbon_results', methods=['GET'])
def get_carbon_results():
    user_url = request.args.get('url')

    if not user_url or not validate_url(user_url):
        return jsonify({"message": "Invalid or missing URL."}), 400
    
    carbon_instance = CarbonAPI(user_url)
    results = carbon_instance.get()
    if results:
        return jsonify({"results": results})
    else:
        return jsonify({"message": "No results found."}), 404

if __name__ == '__main__':
    app.run(debug=True)
