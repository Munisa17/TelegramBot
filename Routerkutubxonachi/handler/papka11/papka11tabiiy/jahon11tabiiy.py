from aiogram import types, Router, F
from aiogram.types import FSInputFile

from Routerkutubxonachi.keyboard.default.fananiqtabiiy11 import fananiqtabiiy11

router = Router()

@router.message(F.text=="🏛 Jahon tarixi-11")
async def send_welcome(message: types.Message):
    doc = FSInputFile("handler/resurs/jahon11.pdf")
    await message.answer_document(document=doc, caption="""🏛 Jahon tarixi darsligi
Bilim sari yana bir qadam qo‘ying

📥 Kitob siz uchun tayyor
✨ Doimo siz bilanmiz!""",reply_markup=fananiqtabiiy11())
