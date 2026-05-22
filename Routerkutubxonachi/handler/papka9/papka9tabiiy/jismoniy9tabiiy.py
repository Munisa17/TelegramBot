from aiogram import types, Router, F
from ....keyboard.default.fananiqtabiiy9 import fananiqtabiiy9
from aiogram.types import FSInputFile

router = Router()

@router.message(F.text=="🏃 Jismoniy tarbiya-9tabiiy")
async def send_welcome(message: types.Message):
    await message.answer(text="""❌ Bu bo'limda hozircha material mavjud emas.""",reply_markup=fananiqtabiiy9())