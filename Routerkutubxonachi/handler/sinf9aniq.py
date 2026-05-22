from aiogram import types, Router, F
from ..keyboard.default.fan9aniq import fan9aniq
from aiogram.types import FSInputFile

router = Router()

@router.message(F.text=="📘 aniq fanlar-9")
async def send_welcome(message: types.Message):

    await message.answer(text="""📖 9-sinf darsliklar markazi

Eng kerakli bilimlar — bir joyda jamlangan

📚 Fanlarni tanlang
📥 Yuklab oling
✨ Va rivojlanishda davom eting

👇 Tanlashni boshlang""",reply_markup=fan9aniq())
