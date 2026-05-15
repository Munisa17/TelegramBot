from aiogram import types, Router, F
from Routerkutubxonachi.keyboard.default.fan8aniq import fan8aniq
from aiogram.types import FSInputFile

router = Router()

@router.message(F.text=="🏃 Jismoniy tarbiya-8aniq")
async def send_welcome(message: types.Message):
    await message.answer(text="""❌ Bu bo'limda hozircha material mavjud emas.""",reply_markup=fan8aniq())