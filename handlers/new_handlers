from aiogram import types
from scraper.scraper import NewsScraper


async def scrape_news(call: types.CallbackQuery):
    global url
    scraper = NewsScraper()
    data = scraper.parse_data_anime()
    for url in data:
        await call.message.answer(
            f"{url}",
        )
    print(url)


def register_news_handlers(dp):
    dp.register_callback_query_handler(scrape_news, lambda call: call.data == "anime_menu")
