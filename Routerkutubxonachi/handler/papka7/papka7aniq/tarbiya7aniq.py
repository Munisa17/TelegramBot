from aiogram import types, Router, F
from ....keyboard.default.fan7aniq import fan7aniq
from aiogram.types import FSInputFile

router = Router()

@router.message(F.text=="🕊️ Tarbiya-7aniq")
async def send_welcome(message: types.Message):
    doc = FSInputFile("handler/resurs/tarbiya7.pdf")
    await message.answer_document(document=doc, caption="""🕊️ Tarbiya darsligi
Bilim sari yana bir qadam qo‘ying

📥 Kitob siz uchun tayyor
✨ Doimo siz bilanmiz!""",reply_markup=fan7aniq())