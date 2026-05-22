from aiogram import types, Router, F
from ....keyboard.default.fan10aniq import fan10aniq
from aiogram.types import FSInputFile

router = Router()

@router.message(F.text=="🏃 Jismoniy tarbiya-10aniq")
async def send_welcome(message: types.Message):
    await message.answer(text="""❌ Bu bo'limda hozircha material mavjud emas.""",reply_markup=fan10aniq())