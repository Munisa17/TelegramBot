from aiogram import types, Router, F
from Routerkutubxonachi.keyboard.default.fan11aniq import fan11aniq
from aiogram.types import FSInputFile

router = Router()

@router.message(F.text=="🏃 Jismoniy tarbiya-11aniq")
async def send_welcome(message: types.Message):
    await message.answer(text="""❌ Bu bo'limda hozircha material mavjud emas.""",reply_markup=fan11aniq())