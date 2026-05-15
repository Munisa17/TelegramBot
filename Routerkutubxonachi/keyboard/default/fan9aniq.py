from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def fan9aniq():
    button = KeyboardButton(text="📖 Ona tili-9aniq")
    button2 = KeyboardButton(text="📘 Adabiyot-9aniq")
    button3 = KeyboardButton(text="🔢 Algebra-9aniq")
    button4 = KeyboardButton(text="📐 Geometriya-9aniq")
    button5 = KeyboardButton(text="🌍 Geografiya-9aniq")
    button6 = KeyboardButton(text="🏛 Tarix(O'zbekiston va jahon tarixi)-9aniq")
    button7 = KeyboardButton(text="🗣 Ingliz tili-9aniq")
    button8 = KeyboardButton(text="⚛️ Fizika-9aniq")
    button9 = KeyboardButton(text="🌱 Biologiya-9aniq")
    button10 = KeyboardButton(text="🎨 ART-9aniq")
    button11 = KeyboardButton(text="💻 Informatika-9aniq")
    button12 = KeyboardButton(text="🏃 Jismoniy tarbiya-9aniq")
    button13 = KeyboardButton(text="🇷🇺 Rus tili-9aniq")
    button14 = KeyboardButton(text="🧪 Kimyo-9aniq")
    button15 = KeyboardButton(text="🕊️ Tarbiya-9aniq")
    button16 = KeyboardButton(text="🤖 Sun'iy intelekt-9aniq")
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