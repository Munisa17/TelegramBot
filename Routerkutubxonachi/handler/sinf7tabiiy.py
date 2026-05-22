from aiogram import types, Router, F
from ..keyboard.default.fan7tabiiy import fan7tabiiy
from aiogram.types import FSInputFile

router = Router()

@router.message(F.text=="🧬 tabiiy fanlar-7")
async def send_welcome(message: types.Message):

    await message.answer(text="""📗 7-sinf darsliklar markazi

Eng kerakli bilimlar — bir joyda jamlangan

📚 Fanlarni tanlang
📥 Yuklab oling
✨ Va rivojlanishda davom eting

👇 Tanlashni boshlang""",reply_markup=fan7tabiiy())
