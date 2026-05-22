from aiogram import types, Router, F
from ....keyboard.default.fan11aniq import fan11aniq
from aiogram.types import FSInputFile

router = Router()

@router.message(F.text=="🪖 Chaqiruvga qadar boshlang'ich tayyorgarlik-11aniq")
async def send_welcome(message: types.Message):
    doc = FSInputFile("handler/resurs/chqbt11.pdf")
    await message.answer_document(document=doc, caption="""🪖 Chaqiruvga qadar boshlang'ich tayyorgarlik darsligi
Bilim sari yana bir qadam qo‘ying

📥 Kitob siz uchun tayyor
✨ Doimo siz bilanmiz!""",reply_markup=fan11aniq())