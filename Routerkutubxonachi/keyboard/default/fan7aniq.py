from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def fan7aniq():
    button = KeyboardButton(text="📖 Ona tili-7aniq")
    button2 = KeyboardButton(text="📘 Adabiyot-7aniq")
    button3 = KeyboardButton(text="🔢 Algebra-7aniq")
    button4 = KeyboardButton(text="📐 Geometriya-7aniq")
    button5 = KeyboardButton(text="🌍 Geografiya-7aniq")
    button6 = KeyboardButton(text="🏛 Tarix(O'zbekiston va jahon tarixi)-7aniq")
    button7 = KeyboardButton(text="🗣 Ingliz tili-7aniq")
    button8 = KeyboardButton(text="⚛️ Fizika-7aniq")
    button9 = KeyboardButton(text="🌱 Biologiya-7aniq")
    button10 = KeyboardButton(text="🎨 ART-7aniq")
    button11 = KeyboardButton(text="💻 Informatika-7aniq")
    button12 = KeyboardButton(text="🏃 Jismoniy tarbiya-7aniq")
    button13 = KeyboardButton(text="🇷🇺 Rus tili-7aniq")
    button14 = KeyboardButton(text="🧪 Kimyo-7aniq")
    button15 = KeyboardButton(text="🕊️ Tarbiya-7aniq")
    button16 = KeyboardButton(text="🤖 Robototexnika-7aniq")
    button17 = KeyboardButton(text="⏪ Orqaga")

    rkm = ReplyKeyboardMarkup(
        keyboard=[
            [button,button2,button3],
            [button4, button5,button6],
            [button7,button8,button9],
            [button10,button11,button12],
            [button13,button14,button15],
            [button16],
            [button17]
        ],
        resize_keyboard=True)
    return rkm