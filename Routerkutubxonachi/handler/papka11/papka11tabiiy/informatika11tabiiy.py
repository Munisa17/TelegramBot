from aiogram import types, Router, F
from ....keyboard.default.fananiqtabiiy10 import fananiqtabiiy10
from aiogram.types import FSInputFile

router = Router()

@router.message(F.text=="💻 Informatika-11tabiiy")
async def send_welcome(message: types.Message):
    doc = FSInputFile("handler/resurs/informatika1011.pdf")
    await message.answer_document(document=doc, caption="""💻 Informatika darsligi
Bilim sari yana bir qadam qo‘ying

📥 Kitob siz uchun tayyor
✨ Doimo siz bilanmiz!""",reply_markup=fananiqtabiiy10())