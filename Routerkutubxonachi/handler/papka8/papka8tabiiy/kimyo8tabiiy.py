from aiogram import types, Router, F
from Routerkutubxonachi.keyboard.default.fananiqtabiiy8 import fananiqtabiiy8
from aiogram.types import FSInputFile

router = Router()

@router.message(F.text=="🧪 Kimyo-8tabiiy")
async def send_welcome(message: types.Message):
    doc = FSInputFile("handler/resurs/kimyo8.pdf")
    await message.answer_document(document=doc, caption="""🧪 Kimyo darsligi
Bilim sari yana bir qadam qo‘ying

📥 Kitob siz uchun tayyor
✨ Doimo siz bilanmiz!""",reply_markup=fananiqtabiiy8())