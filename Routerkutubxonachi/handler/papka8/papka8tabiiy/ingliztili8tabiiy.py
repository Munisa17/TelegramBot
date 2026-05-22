from aiogram import types, Router, F
from ....keyboard.default.fananiqtabiiy8 import fananiqtabiiy8
from aiogram.types import FSInputFile

router = Router()

@router.message(F.text=="🗣 Ingliz tili-8tabiiy")
async def send_welcome(message: types.Message):
    doc = FSInputFile("handler/resurs/ingliztili8.pdf")
    await message.answer_document(document=doc, caption="""🗣 Ingliz tili darsligi
Bilim sari yana bir qadam qo‘ying

📥 Kitob siz uchun tayyor
✨ Doimo siz bilanmiz!""",reply_markup=fananiqtabiiy8())