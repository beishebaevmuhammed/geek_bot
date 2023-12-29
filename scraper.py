from parsel import Selector
import requests


class NewsScraper:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br'
    }

    ANIME_URL = 'https://animespirit.tv/'

    def parse_data_anime(self):
        response = requests.get(self.ANIME_URL, headers=self.headers)
        if response.status_code > 400:
            return []
        selector = Selector(text=response.text)
        all_links = selector.xpath('//div[@class="custom-poster"]/a/@href').getall()

        return all_links


if __name__ == '__main__':
    scraper = NewsScraper()
    print(scraper.parse_data_anime())