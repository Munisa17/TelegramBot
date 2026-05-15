from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def fan8aniq():
    button = KeyboardButton(text="📖 Ona tili-8aniq")
    button2 = KeyboardButton(text="📘 Adabiyot-8aniq")
    button3 = KeyboardButton(text="🔢 Algebra-8aniq")
    button4 = KeyboardButton(text="📐 Geometriya-8aniq")
    button5 = KeyboardButton(text="🌍 Geografiya-8aniq")
    button6 = KeyboardButton(text="🏛 Tarix(O'zbekiston va jahon tarixi)-8aniq")
    button7 = KeyboardButton(text="🗣 Ingliz tili-8aniq")
    button8 = KeyboardButton(text="⚛️ Fizika-8aniq")
    button9 = KeyboardButton(text="🌱 Biologiya-8aniq")
    button10 = KeyboardButton(text="🎨 ART-8aniq")
    button11 = KeyboardButton(text="💻 Informatika-8aniq")
    button12 = KeyboardButton(text="🏃 Jismoniy tarbiya-8aniq")
    button13 = KeyboardButton(text="🇷🇺 Rus tili-8aniq")
    button14 = KeyboardButton(text="🧪 Kimyo-8aniq")
    button15 = KeyboardButton(text="🕊️ Tarbiya-8aniq")
    button16 = KeyboardButton(text="🤖 Robototexnika-8aniq")
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