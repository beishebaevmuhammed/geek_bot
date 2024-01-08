# from aiogram import types
# from scraper.scraper import AnimeScraper
# from scraper.anime_parser import AnimeParser
# from config import bot
#
#
# async def scrape_anime(call: types.CallbackQuery):
#     global url
#     scraper = AnimeScraper()
#     data = scraper.parse_data_anime()
#     for url in data:
#         await call.message.answer(
#             f"{url}",
#         )
#     print(url)
#
#
# async def parser_anime(call: types.CallbackQuery):
#     parser = AnimeParser()
#     anime = parser.parse_data()
#     for key, value in anime.items():
#         await bot.send_photo(
#             chat_id=call.from_user.id,
#             file=value,
#             caption=key
#         )
#
#
# def register_news_handlers(dp):
#     dp.register_callback_query_handler(scrape_anime, lambda call: call.data == "anime_menu")
#     dp.register_callback_query_handler(parser_anime, lambda call: call.data == "parser")
