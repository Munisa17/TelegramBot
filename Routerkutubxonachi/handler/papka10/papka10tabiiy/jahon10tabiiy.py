from aiogram import types, Router, F
from aiogram.types import FSInputFile

from Routerkutubxonachi.keyboard.default.fananiqtabiiy10 import fananiqtabiiy10

router = Router()

@router.message(F.text=="🏛 Jahon tarixi-10")
async def send_welcome(message: types.Message):
    doc = FSInputFile("handler/resurs/jahon10.pdf")
    await message.answer_document(document=doc, caption="""🏛 Jahon tarixi darsligi
Bilim sari yana bir qadam qo‘ying

📥 Kitob siz uchun tayyor
✨ Doimo siz bilanmiz!""",reply_markup=fananiqtabiiy10())
