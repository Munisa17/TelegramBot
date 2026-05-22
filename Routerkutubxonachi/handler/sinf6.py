from aiogram import types, Router, F
from ..keyboard.default.fan6 import fan6

router = Router()

@router.message(F.text=="📘 6-sinf")
async def send_welcome(message: types.Message):

    await message.answer(text="""📘 6-sinf darsliklari olamiga xush kelibsiz!

Har bir fan — yangi bilim va yangi imkoniyat 🚀

📚 O‘zingizga kerakli fanni tanlang
📖 Va o‘qishni boshlang!

👇 Qaysi fan kerak?""",reply_markup=fan6())
