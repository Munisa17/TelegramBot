from aiogram import types, Router, F
from ....keyboard.default.fan9aniq import fan9aniq
from aiogram.types import FSInputFile

router = Router()

@router.message(F.text=="🧪 Kimyo-9aniq")
async def send_welcome(message: types.Message):
    doc = FSInputFile("handler/resurs/kimyo9aniq.pdf")
    await message.answer_document(document=doc, caption="""🧪 Kimyo darsligi
Bilim sari yana bir qadam qo‘ying

📥 Kitob siz uchun tayyor
✨ Doimo siz bilanmiz!""",reply_markup=fan9aniq())