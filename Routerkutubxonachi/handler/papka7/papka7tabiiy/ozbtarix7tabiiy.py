from aiogram import types, Router, F
from ....keyboard.default.fanozbjahon7 import fanozbjahon7
from aiogram.types import FSInputFile

router = Router()

@router.message(F.text=="🏛 O'zbekiston tarixi-7")
async def send_welcome(message: types.Message):
    doc = FSInputFile("handler/resurs/ozbtarix7.pdf")
    await message.answer_document(document=doc, caption="""🏛 O'zbekiston tarixi darsligi
Bilim sari yana bir qadam qo‘ying

📥 Kitob siz uchun tayyor
✨ Doimo siz bilanmiz!""",reply_markup=fanozbjahon7())
