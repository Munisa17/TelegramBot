from aiogram import types, Router, F
from ....keyboard.default.fananiqtabiiy9 import fananiqtabiiy9
from aiogram.types import FSInputFile

router = Router()

@router.message(F.text=="📐 Geometriya-9tabiiy")
async def send_welcome(message: types.Message):
    doc = FSInputFile("handler/resurs/geometriya9.pdf")
    await message.answer_document(document=doc, caption="""📐 Geometriya darsligi
Bilim sari yana bir qadam qo‘ying

📥 Kitob siz uchun tayyor
✨ Doimo siz bilanmiz!""",reply_markup=fananiqtabiiy9())
