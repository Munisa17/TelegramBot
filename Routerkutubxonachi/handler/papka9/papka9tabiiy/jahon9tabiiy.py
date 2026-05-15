from aiogram import types, Router, F
from aiogram.types import FSInputFile

from Routerkutubxonachi.keyboard.default.fananiqtabiiy9 import fananiqtabiiy9

router = Router()

@router.message(F.text=="🏛 Jahon tarixi-9")
async def send_welcome(message: types.Message):
    doc = FSInputFile("handler/resurs/jahon9.pdf")
    await message.answer_document(document=doc, caption="""🏛 Jahon tarixi darsligi
Bilim sari yana bir qadam qo‘ying

📥 Kitob siz uchun tayyor
✨ Doimo siz bilanmiz!""",reply_markup=fananiqtabiiy9())
