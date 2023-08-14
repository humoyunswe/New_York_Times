import requests
import logging

def fetch_news(topic):
    url = f"https://api.nytimes.com/svc/search/v2/articlesearch.json?q={topic}&api-key=oYigdu3MVgGWarxFAVvAJHXcN4cAIxXz"

    try:
        response = requests.get(url)
        data = response.json()
        articles = data.get('response').get('docs')
        return articles

    except requests.exceptions.RequestException as err:
        logging.error(f'Error while fetching news: {err}')
        return []

logging.basicConfig(filename='errors.log',format='%(asctime)s : %(levelname)s : %(message)s')

def main():
    print("You are welcome to the New York Times fetcher!")
    topic = input('Enter the topic you want search for: ')

    articles = fetch_news(topic)

    if not articles:
        print('No information available for the given topic!')
    else:
        print('Hey here some articles related to your search: ')
        for article in articles:
            headline = article.get('headline').get('main')
            snippet = article.get('snippet')
            print(headline)
            print(snippet)
            print()

if __name__ == '__main__':
    main()