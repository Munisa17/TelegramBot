from aiogram import types, Router, F
from Routerkutubxonachi.keyboard.default.fananiqtabiiy8 import fananiqtabiiy8
from aiogram.types import FSInputFile

router = Router()

@router.message(F.text=="📐 Geometriya-8aniq")
async def send_welcome(message: types.Message):
    doc = FSInputFile("handler/resurs/geometriya8aniq.pdf")
    await message.answer_document(document=doc, caption="""📐 Geometriya darsligi
Bilim sari yana bir qadam qo‘ying

📥 Kitob siz uchun tayyor
✨ Doimo siz bilanmiz!""",reply_markup=fananiqtabiiy8())
