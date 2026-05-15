from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def fan9tabiiy():
    button = KeyboardButton(text="📖 Ona tili-9tabiiy")
    button2 = KeyboardButton(text="📘 Adabiyot-9tabiiy")
    button3 = KeyboardButton(text="🔢 Algebra-9tabiiy")
    button4 = KeyboardButton(text="📐 Geometriya-9tabiiy")
    button5 = KeyboardButton(text="🌍 Geografiya-9tabiiy")
    button6 = KeyboardButton(text="🏛 Tarix(O'zbekiston va jahon tarixi)-9tabiiy")
    button7 = KeyboardButton(text="🗣 Ingliz tili-9tabiiy")
    button8 = KeyboardButton(text="⚛️ Fizika-9tabiiy")
    button9 = KeyboardButton(text="🌱 Biologiya-9tabiiy")
    button10 = KeyboardButton(text="🎨 ART-9tabiiy")
    button11 = KeyboardButton(text="💻 Informatika-9tabiiy")
    button12 = KeyboardButton(text="🏃 Jismoniy tarbiya-9tabiiy")
    button13 = KeyboardButton(text="🇷🇺 Rus tili-9tabiiy")
    button14 = KeyboardButton(text="🧪 Kimyo-9tabiiy")
    button15 = KeyboardButton(text="🕊️ Tarbiya-9tabiiy")
    button16 = KeyboardButton(text="🤖 Sun'iy intelekt-9tabiiy")
    button17 = KeyboardButton(text="⏪ Orqaga")

    rkm = ReplyKeyboardMarkup(
        keyboard=[
            [button, button2, button3],
            [button4, button5, button6],
            [button7, button8, button9],
            [button10, button11, button12],
            [button13, button14, button15],
            [button16],
            [button17]
        ],
        resize_keyboard=True)
    return rkm