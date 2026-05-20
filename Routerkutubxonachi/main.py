from aiogram import Bot, Dispatcher
from handler import setup_message_routers
import asyncio
import logging
# from aiogram.enums import ParseMode
from config import TOKEN,ADMINS
bot = Bot(token=TOKEN)
dp = Dispatcher()



async def on_startup(dispatcher: Dispatcher):
    """Bot ishga tushganda admin userga xabar yuboradi."""
    # await bot.send_message(chat_id=str(ADMINS), text="Bot ishga tushdi")
    # logging.info("Bot ishga tushganligi haqida xabar yuborildi.")


async def main():
    # Routerlarni sozlash
    handler_router = setup_message_routers()
    dp.include_router(handler_router)

    # Dispatcher signalini sozlash
    dp.startup.register(on_startup)

    # Eski yangilanishlarni o'chirish
    await bot.delete_webhook(drop_pending_updates=True)

    # Pollingni boshlash
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
