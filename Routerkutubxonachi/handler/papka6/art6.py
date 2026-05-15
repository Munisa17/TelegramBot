from aiogram import types, Router, F
from Routerkutubxonachi.keyboard.default.fan6 import fan6
from aiogram.types import FSInputFile

router = Router()

@router.message(F.text=="🎨 ART-6")
async def send_welcome(message: types.Message):
    doc = FSInputFile("handler/resurs/art6.pdf")
    await message.answer_document(document=doc, caption="""🎨 ART darsligi
Bilim sari yana bir qadam qo‘ying

📥 Kitob siz uchun tayyor
✨ Doimo siz bilanmiz!""",reply_markup=fan6())