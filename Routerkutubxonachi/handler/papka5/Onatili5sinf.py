from aiogram import types, Router, F
from Routerkutubxonachi.keyboard.default.fan5 import fan5
from aiogram.types import FSInputFile

router = Router()

@router.message(F.text=="📖 Ona tili-5")
async def send_document(message: types.Message):
    doc = FSInputFile("handler/resurs/onatili1qism5.pdf")
    await message.answer_document(document=doc, caption="""📖 Ona tili darsligi
Bilim sari yana bir qadam qo‘ying

📥 Kitob siz uchun tayyor
✨ Doimo siz bilanmiz!""",reply_markup=fan5())