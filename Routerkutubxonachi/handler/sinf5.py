from aiogram import types, Router, F
from Routerkutubxonachi.keyboard.default.fan5 import fan5

router = Router()

@router.message(F.text=="📚 5-sinf")
async def send_welcome(message: types.Message):

    await message.answer(text="""📚 5-sinf darsliklari olamiga xush kelibsiz!

Har bir fan — yangi bilim va yangi imkoniyat 🚀

📚 O‘zingizga kerakli fanni tanlang
📖 Va o‘qishni boshlang!

👇 Qaysi fan kerak?""",reply_markup=fan5())
