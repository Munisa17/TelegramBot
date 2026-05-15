from aiogram import types, Router, F
from Routerkutubxonachi.keyboard.default.fan5 import fan5


router = Router()

@router.message(F.text=="🏃 Jismoniy tarbiya-5")
async def send_welcome(message: types.Message):
    await message.answer(text="""❌ Bu bo'limda hozircha material mavjud emas.""",reply_markup=fan5())
