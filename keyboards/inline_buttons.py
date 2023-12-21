from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def start_menu_keyboard():
    markup = InlineKeyboardMarkup()
    questionnaire_button = InlineKeyboardButton(
        "Начинать",
        callback_data="Start_questionnaire"
    )

    registration_button = InlineKeyboardButton(
        "Регистрация❤️",
        callback_data="регистрация"
    )
    markup.add(questionnaire_button)
    markup.add(registration_button)
    return markup


async def start_1questionnaire_keyboard():
    markup = InlineKeyboardMarkup()
    question1_button = InlineKeyboardButton(
        "Python🐍",
        callback_data="python"
    )
    question2_button = InlineKeyboardButton(
        "JavaScript😎",
        callback_data="javaScript"
    )
    question3_button = InlineKeyboardButton(
        "C++🤓",
        callback_data="c++"
    )
    markup.add(question1_button)
    markup.add(question2_button)
    markup.add(question3_button)
    return markup


async def start_2questionnaire_keyboard():
    markup = InlineKeyboardMarkup()
    question4_button = InlineKeyboardButton(
        "Macbook Pro 14 M2 MAX",
        callback_data="Macbook Pro 14 M2 MAX"
    )

    question5_button = InlineKeyboardButton(
        "Acer Swift 3X",
        callback_data="Acer Swift 3X"
    )

    question6_button = InlineKeyboardButton(
        "Asus Chromebook Flip CX5",
        callback_data="Asus Chromebook Flip CX5"
    )

    markup.add(question4_button)
    markup.add(question5_button)
    markup.add(question6_button)
    return markup


async def start_3questionnaire_keyboard():
    markup = InlineKeyboardMarkup()
    question7_button = InlineKeyboardButton(
        "В кофейне",
        callback_data="В кофейне"
    )

    question8_button = InlineKeyboardButton(
        "В универе",
        callback_data="В универе"
    )

    question9_button = InlineKeyboardButton(
        "В geeks",
        callback_data="В geeks"
    )

    markup.add(question7_button)
    markup.add(question8_button)
    markup.add(question9_button)
    return markup
