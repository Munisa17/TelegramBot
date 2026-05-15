from aiogram import types, Router, F
from Routerkutubxonachi.keyboard.default.fan11tabiiy import fan11tabiiy
from aiogram.types import FSInputFile

router = Router()

@router.message(F.text=="🧬 tabiiy fanlar-11")
async def send_welcome(message: types.Message):

    await message.answer(text="""🏆 11-sinf darsliklar markazi

Eng kerakli bilimlar — bir joyda jamlangan

📚 Fanlarni tanlang
📥 Yuklab oling
✨ Va rivojlanishda davom eting

👇 Tanlashni boshlang""",reply_markup=fan11tabiiy())
