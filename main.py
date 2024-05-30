import asyncio
import os

from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode

from config import TOKEN
from headers.message_handlers import router



bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)

dp = Dispatcher()

dp.include_router(router)


async def on_startup():
    print("Bot Started")


async def on_shutdown():
    print("Bot Shutdown")


async def main():
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


asyncio.run(main())
