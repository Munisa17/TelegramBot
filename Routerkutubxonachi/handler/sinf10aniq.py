from aiogram import types, Router, F
from ..keyboard.default.fan10aniq import fan10aniq
from aiogram.types import FSInputFile

router = Router()

@router.message(F.text=="📘 aniq fanlar-10")
async def send_welcome(message: types.Message):

    await message.answer(text="""🎓 10-sinf darsliklar markazi

Eng kerakli bilimlar — bir joyda jamlangan

📚 Fanlarni tanlang
📥 Yuklab oling
✨ Va rivojlanishda davom eting

👇 Tanlashni boshlang""",reply_markup=fan10aniq())
