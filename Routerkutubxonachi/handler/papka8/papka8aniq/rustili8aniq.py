from aiogram import types, Router, F
from Routerkutubxonachi.keyboard.default.fan8aniq import fan8aniq
from aiogram.types import FSInputFile

router = Router()

@router.message(F.text=="🇷🇺 Rus tili-8aniq")
async def send_welcome(message: types.Message):
    doc = FSInputFile("handler/resurs/rustili8.pdf")
    await message.answer_document(document=doc, caption="""🇷🇺 Rus tili darsligi
Bilim sari yana bir qadam qo‘ying

📥 Kitob siz uchun tayyor
✨ Doimo siz bilanmiz!""",reply_markup=fan8aniq())