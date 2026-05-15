from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def fan5():
    button = KeyboardButton(text="📖 Ona tili-5")
    button2 = KeyboardButton(text="📘 Adabiyot-5")
    button3 = KeyboardButton(text="🔢 Matematika-5")
    button4 = KeyboardButton(text="🌍 Tabiiy fan-5")
    button5 = KeyboardButton(text="🏛 Tarix-5")
    button6 = KeyboardButton(text="🗣 Ingliz tili-5")
    button7 = KeyboardButton(text="🎨 ART-5")
    button8 = KeyboardButton(text="💻 Informatika-5")
    button9 = KeyboardButton(text="🏃 Jismoniy tarbiya-5")
    button10=KeyboardButton(text="🤝 Tarbiya-5")
    button11 = KeyboardButton(text ="🇷🇺 Rus tili-5")
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