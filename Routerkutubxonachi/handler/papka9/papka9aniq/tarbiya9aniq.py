from aiogram import types, Router, F
from Routerkutubxonachi.keyboard.default.fan9aniq import fan9aniq
from aiogram.types import FSInputFile

router = Router()

@router.message(F.text=="🕊️ Tarbiya-9aniq")
async def send_welcome(message: types.Message):
    doc = FSInputFile("handler/resurs/tarbiya9.pdf")
    await message.answer_document(document=doc, caption="""🕊️ Tarbiya darsligi
Bilim sari yana bir qadam qo‘ying

📥 Kitob siz uchun tayyor
✨ Doimo siz bilanmiz!""",reply_markup=fan9aniq())