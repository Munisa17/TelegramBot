from aiogram import types, Router, F
from Routerkutubxonachi.keyboard.default.fan9tabiiy import fan9tabiiy
from aiogram.types import FSInputFile

router = Router()

@router.message(F.text=="🧬 tabiiy fanlar-9")
async def send_welcome(message: types.Message):

    await message.answer(text="""📖 9-sinf darsliklar markazi

Eng kerakli bilimlar — bir joyda jamlangan

📚 Fanlarni tanlang
📥 Yuklab oling
✨ Va rivojlanishda davom eting

👇 Tanlashni boshlang""",reply_markup=fan9tabiiy())
