from aiogram import types, Router, F
from ..keyboard.default.fan8aniq import fan8aniq
from aiogram.types import FSInputFile

router = Router()

@router.message(F.text=="📘 aniq fanlar-8")
async def send_welcome(message: types.Message):

    await message.answer(text="""📙 8-sinf darsliklar markazi

Eng kerakli bilimlar — bir joyda jamlangan

📚 Fanlarni tanlang
📥 Yuklab oling
✨ Va rivojlanishda davom eting

👇 Tanlashni boshlang""",reply_markup=fan8aniq())
