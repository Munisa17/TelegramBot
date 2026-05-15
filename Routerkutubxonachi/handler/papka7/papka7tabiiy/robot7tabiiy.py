from aiogram import types, Router, F
from Routerkutubxonachi.keyboard.default.fananiqtabiiy7 import fananiqtabiiy7
from aiogram.types import FSInputFile

router = Router()

@router.message(F.text=="🤖 Robototexnika-7tabiiy")
async def send_welcome(message: types.Message):
    await message.answer(text="""❌ Bu bo'limda hozircha material mavjud emas.""",reply_markup=fananiqtabiiy7())