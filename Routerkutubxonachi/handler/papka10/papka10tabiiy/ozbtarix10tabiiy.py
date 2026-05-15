from aiogram import types, Router, F
from Routerkutubxonachi.keyboard.default.fanozbjahon10 import fanozbjahon10
from aiogram.types import FSInputFile

router = Router()

@router.message(F.text=="🏛 O'zbekiston tarixi-10")
async def send_welcome(message: types.Message):
    doc = FSInputFile("handler/resurs/ozbtarix10.pdf")
    await message.answer_document(document=doc, caption="""🏛 O'zbekiston tarixi darsligi
Bilim sari yana bir qadam qo‘ying

📥 Kitob siz uchun tayyor
✨ Doimo siz bilanmiz!""",reply_markup=fanozbjahon10())
