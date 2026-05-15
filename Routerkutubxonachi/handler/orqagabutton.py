from aiogram import types, Router, F
from Routerkutubxonachi.keyboard.default.main_keyboard import menu

router = Router()

@router.message(F.text == "⏪ Orqaga")
async def send_welcome(message: types.Message):
    await message.answer(text="orqaga qaytildi",reply_markup=menu())
