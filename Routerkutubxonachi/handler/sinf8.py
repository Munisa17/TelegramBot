from aiogram import types, Router, F
from ..keyboard.default.fananiqtabiiy8 import fananiqtabiiy8

router = Router()

@router.message(F.text=="📙 8-sinf")
async def send_welcome(message: types.Message):

    await message.answer(text="""✨ 8-sinf fanlari quyidagi yo‘nalishlarga bo‘lingan:
📏 Aniq fanlar — hisob-kitob va mantiq
🌱 Tabiiy fanlar — tabiat va hayot haqidagi bilimlar
Kerakli bo‘limni tanlang 🚀""",reply_markup=fananiqtabiiy8())
