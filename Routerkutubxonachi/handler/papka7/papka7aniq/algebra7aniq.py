from aiogram import types, Router, F
from Routerkutubxonachi.keyboard.default.fananiqtabiiy7 import fananiqtabiiy7
from aiogram.types import FSInputFile

router = Router()

@router.message(F.text=="🔢 Algebra-7aniq")
async def send_welcome(message: types.Message):
    doc = FSInputFile("handler/resurs/algebra7.pdf")
    await message.answer_document(document=doc, caption="""🔢 Algebra darsligi
Bilim sari yana bir qadam qo‘ying

📥 Kitob siz uchun tayyor
✨ Doimo siz bilanmiz!""",reply_markup=fananiqtabiiy7())
