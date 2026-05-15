from aiogram import types, Router, F
from Routerkutubxonachi.keyboard.default.fan10aniq import fan10aniq
from aiogram.types import FSInputFile

router = Router()

@router.message(F.text=="🧪 Kimyo-10aniq")
async def send_welcome(message: types.Message):
    doc = FSInputFile("handler/resurs/kimyo10.pdf")
    await message.answer_document(document=doc, caption="""🧪 Kimyo darsligi
Bilim sari yana bir qadam qo‘ying

📥 Kitob siz uchun tayyor
✨ Doimo siz bilanmiz!""",reply_markup=fan10aniq())