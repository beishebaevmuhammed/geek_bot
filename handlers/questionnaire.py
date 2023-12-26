
from aiogram import types, Dispatcher
from config import bot
from keyboards import inline_buttons


async def start_questionnaire_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Какой язык Ты выберешь?",
        reply_markup=await inline_buttons.start_1questionnaire_keyboard()
    )


async def question1_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="О, классно😍 "
             "Тогда давай теперь выберем ноутбук: ",
        reply_markup=await inline_buttons.start_2questionnaire_keyboard()
    )


async def question2_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Супер👍 "
             "Тогда давай теперь выберем ноутбук: ",
        reply_markup=await inline_buttons.start_2questionnaire_keyboard()
    )


async def question3_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Молодец👍 "
             "Тогда давай теперь выберем ноутбук: ",
        reply_markup=await inline_buttons.start_2questionnaire_keyboard()
    )


async def question6_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Смотрю неплохо зарабатываешь😏 "
             "И где Ты в основном проводишь свое время?",
        reply_markup=await inline_buttons.start_3questionnaire_keyboard()
    )


async def question7_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Творческий человек🙂 "
             "И где Ты в основном проводишь свое время?",
        reply_markup=await inline_buttons.start_3questionnaire_keyboard()
    )


async def question8_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Выбрал ноутбук чисто для учебы и программирования👍 "
             "И где Ты в основном проводишь свое время?",
        reply_markup=await inline_buttons.start_3questionnaire_keyboard()
    )


async def question9_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Деловой такой😎 ",
    )


async def question10_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Сессии начались🫠 ",
    )


async def question11_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Ооо, из наших значит, респект🤝",
    )


def register_questionnaire_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(start_questionnaire_call,
                                       lambda call: call.data == "Start_questionnaire")
    dp.register_callback_query_handler(question1_call,
                                       lambda call: call.data == "python")
    dp.register_callback_query_handler(question2_call,
                                       lambda call: call.data == "javaScript")
    dp.register_callback_query_handler(question3_call,
                                       lambda call: call.data == "c++")
    dp.register_callback_query_handler(question6_call,
                                       lambda call: call.data == "Macbook Pro 14 M2 MAX")
    dp.register_callback_query_handler(question7_call,
                                       lambda call: call.data == "Acer Swift 3X")
    dp.register_callback_query_handler(question8_call,
                                       lambda call: call.data == "Asus Chromebook Flip CX5")
    dp.register_callback_query_handler(question9_call,
                                       lambda call: call.data == "В кофейне")
    dp.register_callback_query_handler(question10_call,
                                       lambda call: call.data == "В универе")
    dp.register_callback_query_handler(question11_call,
                                       lambda call: call.data == "В geeks")
