from aiogram import types, Router, F
from Routerkutubxonachi.keyboard.default.fanozbjahon8 import fanozbjahon8
from aiogram.types import FSInputFile

router = Router()

@router.message(F.text=="🏛 O'zbekiston tarixi-8")
async def send_welcome(message: types.Message):
    doc = FSInputFile("handler/resurs/ozbtarix8.pdf")
    await message.answer_document(document=doc, caption="""🏛 O'zbekiston tarixi darsligi
Bilim sari yana bir qadam qo‘ying

📥 Kitob siz uchun tayyor
✨ Doimo siz bilanmiz!""",reply_markup=fanozbjahon8())
