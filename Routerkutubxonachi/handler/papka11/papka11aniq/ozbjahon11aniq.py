from aiogram import types, Router, F
from ....keyboard.default.fanozbjahon11 import fanozbjahon11

router = Router()

@router.message(F.text=="🏛 Tarix(O'zbekiston va jahon tarixi)-11aniq")
async def send_welcome(message: types.Message):
    await message.answer(text="""🏛 Tarix bo‘limiga xush kelibsiz!
Iltimos, quyidagilardan birini tanlang:
🇺🇿 O‘zbekiston tarixi
🌍 Jahon tarixi""",reply_markup=fanozbjahon11())
