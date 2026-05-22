from aiogram import types, Router, F
from ....keyboard.default.fan9aniq import fan9aniq
from aiogram.types import FSInputFile

router = Router()

@router.message(F.text=="🇷🇺 Rus tili-9aniq")
async def send_welcome(message: types.Message):
    doc = FSInputFile("handler/resurs/rustili9.pdf")
    await message.answer_document(document=doc, caption="""🇷🇺 Rus tili darsligi
Bilim sari yana bir qadam qo‘ying

📥 Kitob siz uchun tayyor
✨ Doimo siz bilanmiz!""",reply_markup=fan9aniq())