from aiogram import types, Router, F
from ....keyboard.default.fanozbjahon9 import fanozbjahon9

router = Router()

@router.message(F.text=="🏛 Tarix(O'zbekiston va jahon tarixi)-9tabiiy")
async def send_welcome(message: types.Message):
    await message.answer(text="""🏛 Tarix bo‘limiga xush kelibsiz!
Iltimos, quyidagilardan birini tanlang:
🇺🇿 O‘zbekiston tarixi
🌍 Jahon tarixi""",reply_markup=fanozbjahon9())
