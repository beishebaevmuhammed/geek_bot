import random
import re
import sqlite3
import  os
import binascii
from aiogram import types, Dispatcher
from aiogram.utils.deep_linking import _create_link
from config import bot
from const import REFERENCE_MENU_TEXT
from database.sql_commands import Database
from keyboards.inline_buttons import reference_menu_keyboard


async def reference_menu_call(call: types.CallbackQuery):
    db = Database()
    data = db.sql_reference_menu_data(
        tg_id=call.from_user.id,
    )
    await bot.send_message(
        chat_id=call.from_user.id,
        text=REFERENCE_MENU_TEXT.format(
            user=call.from_user.first_name,
            balance=data['balance'],
            referral=data['total_referral']
        ),
        reply_markup=await reference_menu_keyboard()
    )

async def reference_list_call(call: types.CallbackQuery):
        db = Database()
        referral_count = db.reference_menu_data(
            tg_id=call.from_user.id
        )
        referral_list = db.sql_select_referral_user(
            referral_first_name=call.from_user.first_name
        )
        if not referral_list:
            await bot.send_message(
                chat_id=call.from_user.id,
                text="У вас нету рефералов!!!"
            )
        else:
            await bot.send_message(
                chat_id=call.from_user.id,
                text=REFERENCE_COUNT_TEXT.format(
                    total_referral=referral_count,
                    first_name=referral_list
                )
            )

async def reference_link_call(call: types.CallbackQuery):
    db = Database()
    user = db.sql_select_user(
        tg_id=call.from_user.id
    )
    print(user)
    if not user['link']:
        token = binascii.hexlify(os.urandom(10)).decode()
        link = await _create_link(link_type="start", payload=token)
        db.sql_update_user_link(
            link=link,
            tg_id=call.from_user.id,
        )
        await bot.send_message(
            chat_id=call.from_user.id,
            text=f"Here is ur new link: {link}"
        )
    else:
        await bot.send_message(
            chat_id=call.from_user.id,
            text=f"Here is ur old link: {user['link']}"
        )
def register_reference_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(
        reference_menu_call,
        lambda call: call.data == 'reference_menu'
    )
    dp.register_callback_query_handler(
        reference_link_call,
        lambda call: call.data == 'reference_link'
    )
    dp.register_callback_query_handler(
        reference_list_call,
        lambda call: call.data == 'reference_list'
    )