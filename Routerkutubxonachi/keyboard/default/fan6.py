from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def fan6():
    button = KeyboardButton(text="📖 Ona tili-6")
    button2 = KeyboardButton(text="📘 Adabiyot-6")
    button3 = KeyboardButton(text="🔢 Matematika-6")
    button4 = KeyboardButton(text="🤝 Tarbiya-6")
    button5 = KeyboardButton(text="🏛 Tarix-6")
    button6 = KeyboardButton(text="🗣 Ingliz tili-6")
    button7 = KeyboardButton(text="🎨 ART-6")
    button8 = KeyboardButton(text="💻 Informatika-6")
    button9 = KeyboardButton(text="🏃 Jismoniy tarbiya-6")
    button10 = KeyboardButton(text="🇷🇺 Rus tili-6")
    button11 = KeyboardButton(text="🌍 Tabiiy fan-6")
    button12 = KeyboardButton(text="⏪ Orqaga")

    rkm = ReplyKeyboardMarkup(
        keyboard=[
            [button, button2, button3],
            [button4, button5, button6],
            [button7, button8, button9],
            [button10, button11],
            [button12]
        ],
        resize_keyboard=True)
    return rkm