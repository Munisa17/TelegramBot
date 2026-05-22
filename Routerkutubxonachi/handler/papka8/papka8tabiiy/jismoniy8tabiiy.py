from aiogram import types, Router, F
from ....keyboard.default.fananiqtabiiy8 import fananiqtabiiy8
from aiogram.types import FSInputFile

router = Router()

@router.message(F.text=="🏃 Jismoniy tarbiya-8tabiiy")
async def send_welcome(message: types.Message):
    await message.answer(text="""❌ Bu bo'limda hozircha material mavjud emas.""",reply_markup=fananiqtabiiy8())