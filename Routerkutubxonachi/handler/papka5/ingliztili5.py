from aiogram import types, Router, F
from ...keyboard.default.fan5 import fan5
from aiogram.types import FSInputFile

router = Router()

@router.message(F.text=="🗣 Ingliz tili-5")
async def send_welcome(message: types.Message):
    doc = FSInputFile("handler/resurs/ingliztili5.pdf")
    await message.answer_document(document=doc, caption="""🗣 Ingliz tili darsligi
Bilim sari yana bir qadam qo‘ying

📥 Kitob siz uchun tayyor
✨ Doimo siz bilanmiz!""",reply_markup=fan5())