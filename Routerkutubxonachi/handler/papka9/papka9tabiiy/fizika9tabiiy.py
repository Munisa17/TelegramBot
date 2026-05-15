from aiogram import types, Router, F
from Routerkutubxonachi.keyboard.default.fananiqtabiiy9 import fananiqtabiiy9
from aiogram.types import FSInputFile

router = Router()

@router.message(F.text=="⚛️ Fizika-9tabiiy")
async def send_welcome(message: types.Message):
    doc = FSInputFile("handler/resurs/fizika9tabiiy.pdf")
    await message.answer_document(document=doc, caption="""⚛️ Fizika darsligi
Bilim sari yana bir qadam qo‘ying

📥 Kitob siz uchun tayyor
✨ Doimo siz bilanmiz!""",reply_markup=fananiqtabiiy9())