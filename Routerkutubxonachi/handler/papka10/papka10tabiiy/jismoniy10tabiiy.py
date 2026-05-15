from aiogram import types, Router, F
from Routerkutubxonachi.keyboard.default.fananiqtabiiy10 import fananiqtabiiy10
from aiogram.types import FSInputFile

router = Router()

@router.message(F.text=="🏃 Jismoniy tarbiya-10tabiiy")
async def send_welcome(message: types.Message):
    await message.answer(text="""❌ Bu bo'limda hozircha material mavjud emas.""",reply_markup=fananiqtabiiy10())