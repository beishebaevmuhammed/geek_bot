from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from config import bot, MEDIA_DESTINATION
from const import PROFILE_TEXT
from database.sql_commands import Database


class RegistrationStates(StatesGroup):
    nickname = State()
    biography = State()
    age = State()
    gender = State()
    city = State()
    relationship_status = State()
    photo = State()


async def start_registration(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text='Твой никнейм?'
    )
    await RegistrationStates.nickname.set()


async def load_nickname(message: types.Message,
                        state: FSMContext):
    async with state.proxy() as data:
        data['nickname'] = message.text
        print(data)

    await bot.send_message(
        chat_id=message.from_user.id,
        text='Расскажи о себе'
    )
    await RegistrationStates.next()


async def load_biography(message: types.Message,
                         state: FSMContext):
    async with state.proxy() as data:
        data['biography'] = message.text
        print(data)

    await bot.send_message(
        chat_id=message.from_user.id,
        text='Сколько Тебе лет?'
    )

    await RegistrationStates.next()


async def load_age(message: types.Message,
                   state: FSMContext):
    try:
        type(int(message.text))
    except ValueError:
        await bot.send_message(
            chat_id=message.from_user.id,
            text='I said send me only numeric answer\n'
                 'Re-Registration, ur state of registration is over!!!'
        )
        await state.finish()
        return

    async with state.proxy() as data:
        data['age'] = message.text
        print(data)

    await bot.send_message(
        chat_id=message.from_user.id,
        text='Твой гендер?'
    )

    await RegistrationStates.next()


async def load_gender(message: types.Message,
                      state: FSMContext):
    async with state.proxy() as data:
        data['gender'] = message.text
        print(data)

    await bot.send_message(
        chat_id=message.from_user.id,
        text='Ты из какого города?'
    )

    await RegistrationStates.next()


async def load_city(message: types.Message,
                    state: FSMContext):
    async with state.proxy() as data:
        data['city'] = message.text
        print(data)

    await bot.send_message(
        chat_id=message.from_user.id,
        text='Твой статус отношений?'
    )

    await RegistrationStates.next()


async def load_relationship_status(message: types.Message,
                                   state: FSMContext):
    async with state.proxy() as data:
        data['relationship_status'] = message.text
        print(data)

    await bot.send_message(
        chat_id=message.from_user.id,
        text='Отправь свою фотографию.'
    )

    await RegistrationStates.next()


async def load_photo(message: types.Message,
                     state: FSMContext):
    db = Database()
    print(message.photo)
    path = await message.photo[-1].download(
        destination_dir=MEDIA_DESTINATION
    )
    print(path.name)
    async with state.proxy() as data:
        db.sql_insert_profile(
            tg_id=message.from_user.id,
            nickname=data['nickname'],
            biography=data['biography'],
            age=data['age'],
            gender=data['gender'],
            city=data['city'],
            relationship_status=data['relationship_status'],
            photo=path.name
        )
        with open(path.name, 'rb') as photo:
            await bot.send_photo(
                chat_id=message.from_user.id,
                photo=photo,
                caption=PROFILE_TEXT.format(
                    nickname=data['nickname'],
                    biography=data['biography'],
                    age=data['age'],
                    gender=data['gender'],
                    city=data['city'],
                    relationship_status=data['relationship_status'],
                ),
                parse_mode=types.ParseMode.MARKDOWN
            )
        await bot.send_message(
            chat_id=message.from_user.id,
            text='Ты успешно зарегистрировался👍'
        )

        await state.finish()


def register_registration_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(
        start_registration,
        lambda call: call.data == "регистрация"
    )
    dp.register_message_handler(
        load_nickname,
        state=RegistrationStates.nickname,
        content_types=['text']
    )
    dp.register_message_handler(
        load_biography,
        state=RegistrationStates.biography,
        content_types=['text']
    )
    dp.register_message_handler(
        load_age,
        state=RegistrationStates.age,
        content_types=['text']
    )
    dp.register_message_handler(
        load_gender,
        state=RegistrationStates.gender,
        content_types=['text']
    )
    dp.register_message_handler(
        load_city,
        state=RegistrationStates.city,
        content_types=['text']
    )
    dp.register_message_handler(
        load_relationship_status,
        state=RegistrationStates.relationship_status,
        content_types=['text']
    )
    dp.register_message_handler(
        load_photo,
        state=RegistrationStates.photo,
        content_types=types.ContentTypes.PHOTO
    )
