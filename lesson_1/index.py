import asyncio

from aiogram.types import ReplyKeyboardMarkup, Message, WebAppInfo
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from token_api import TOKEN_API
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart, Command

dp = Dispatcher()

web_app_url = "https://thunderous-trifle-98fe71.netlify.app/"
web_app_info = WebAppInfo(url=web_app_url)

def keyboard():
    builder = ReplyKeyboardBuilder()
    builder.button(text='入局')
    builder.button(text='註冊/登入')
    builder.button(text='牌組設定', web_app=web_app_info)
    builder.button(text='儀表板')
    builder.adjust(2, 2)

    return builder.as_markup(resize_keyboard = True)

@dp.message(CommandStart())
async def cmd_start(msg: types.Message) -> None:
    await msg.answer(
        text='Hello World!'
    )

@dp.message(Command('keyboard'))
async def command_keyboard_handler(message: Message) -> None:
    await message.answer(f"Tap the button", reply_markup=keyboard())

async def main() -> None:
    bot = Bot(TOKEN_API)

    print('Start Polling...')
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
