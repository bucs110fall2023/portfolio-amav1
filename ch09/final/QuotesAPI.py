import requests
import random

class QuotesAPI:
    def __init__(self):
        self.url = "https://quotesondesign.com/wp-json/wp/v2/posts/?orderby=rand"
        self.fetched_quotes = []

    def daily_inspiration(self):
        url = self.url
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
       
        if data:
            unique_quotes = [quote_data['content']['rendered'] for quote_data in data if 'content' in quote_data]
            available_quotes = [quote for quote in unique_quotes if quote not in self.fetched_quotes]
            if available_quotes:
                selected_quote = random.choice(available_quotes)
                self.fetched_quotes.append(selected_quote)
                return selected_quote
        return ""