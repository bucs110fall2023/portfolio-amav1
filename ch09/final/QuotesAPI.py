import requests

class QuotesAPI:
    def __init__(self):
        self.url = "https://quotesondesign.com/wp-json/wp/v2/posts/?orderby=rand"

    def daily_inspiration(self):
        url = self.url
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        if data:
            quote_data = []
            for quote_data in data:
                if 'content' in quote_data:
                    return quote_data['content']['rendered']  
        return "" 
