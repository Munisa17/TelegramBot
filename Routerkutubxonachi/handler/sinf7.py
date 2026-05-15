from aiogram import types, Router, F
from Routerkutubxonachi.keyboard.default.fananiqtabiiy7 import fananiqtabiiy7

router = Router()

@router.message(F.text=="📗 7-sinf")
async def send_welcome(message: types.Message):

    await message.answer(text="""✨ 7-sinf fanlari quyidagi yo‘nalishlarga bo‘lingan:
📏 Aniq fanlar — hisob-kitob va mantiq
🌱 Tabiiy fanlar — tabiat va hayot haqidagi bilimlar
Kerakli bo‘limni tanlang 🚀""",reply_markup=fananiqtabiiy7())
