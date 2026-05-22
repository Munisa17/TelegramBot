from aiogram import types, Router, F
from ....keyboard.default.fan7aniq import fan7aniq
from aiogram.types import FSInputFile

router = Router()

@router.message(F.text=="🏃 Jismoniy tarbiya-7aniq")
async def send_welcome(message: types.Message):
    await message.answer(text="""❌ Bu bo'limda hozircha material mavjud emas.""",reply_markup=fan7aniq())