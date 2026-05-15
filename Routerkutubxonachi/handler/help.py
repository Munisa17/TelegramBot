from aiogram import types, Router
from aiogram.filters import Command

router = Router()


@router.message(Command("help"))
async def send_welcome(message: types.Message):
    await message.answer(text="""Kutubxonachi botdan foydalanish juda oson:

📌 Kerakli sinfni tanlang (5–11)
📚 Sizga mos darsliklar ro‘yxati chiqadi
📥 Istagan kitobingizni PDF formatda yuklab oling

Agar botda xatolik topsangiz yoki qo‘shimcha kitob kerak bo‘lsa — bemalol yozing 👇

👩‍💻 Admin: @omg_mia

✨ Siz uchun doimo yangilanib boramiz!""")