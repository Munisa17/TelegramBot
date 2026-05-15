from aiogram import types, Router, F
from aiogram.filters import Command
from Routerkutubxonachi.keyboard.default.main_keyboard import menu

router = Router()


@router.message(Command("start"))
async def send_welcome(message: types.Message):
    await message.answer(text=f"""Salom {message.from_user.first_name}!
———    ✨ Welcome to *Kutubxonachi Bot* 📚

Bu yerda bilim — birgina tugma masofasida.

🎓 5–11-sinflar uchun barcha darsliklar
⚡️ Tezkor va qulay qidiruv
📥 PDF formatda yuklab olish imkoniyati

📖 O‘zingizga kerakli sinfni tanlang
va o‘qishni hoziroq boshlang!""",reply_markup=menu())

