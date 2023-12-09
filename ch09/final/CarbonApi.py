import requests

class CarbonAPI: 
    def __init__(self, url):
        self.api_url = 'https://api.websitecarbon.com/url/' + url  
    
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

def main():
    user_url = input("Enter the URL you want to check: ")
    carbon_instance = CarbonAPI(user_url)
    results = carbon_instance.get()
    if results:
        print(results)
    else:
        print("No results found.")

if __name__ == "__main__":
    main()
