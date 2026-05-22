from aiogram import types, Router, F
from ....keyboard.default.fananiqtabiiy11 import fananiqtabiiy11
from aiogram.types import FSInputFile

router = Router()

@router.message(F.text=="🇷🇺 Rus tili-11tabiiy")
async def send_welcome(message: types.Message):
    doc = FSInputFile("handler/resurs/rustili11.pdf")
    await message.answer_document(document=doc, caption="""🇷🇺 Rus tili darsligi
Bilim sari yana bir qadam qo‘ying

📥 Kitob siz uchun tayyor
✨ Doimo siz bilanmiz!""",reply_markup=fananiqtabiiy11())