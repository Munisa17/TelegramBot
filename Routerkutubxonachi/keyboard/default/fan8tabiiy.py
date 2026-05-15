from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def fan8tabiiy():
    button = KeyboardButton(text="📖 Ona tili-8tabiiy")
    button2 = KeyboardButton(text="📘 Adabiyot-8tabiiy")
    button3 = KeyboardButton(text="🔢 Algebra-8tabiiy")
    button4 = KeyboardButton(text="📐 Geometriya-8tabiiy")
    button5 = KeyboardButton(text="🌍 Geografiya-8tabiiy")
    button6 = KeyboardButton(text="🏛 Tarix(O'zbekiston va jahon tarixi)-8tabiiy")
    button7 = KeyboardButton(text="🗣 Ingliz tili-8tabiiy")
    button8 = KeyboardButton(text="⚛️ Fizika-8tabiiy")
    button9 = KeyboardButton(text="🌱 Biologiya-8tabiiy")
    button10 = KeyboardButton(text="🎨 ART-8tabiiy")
    button11 = KeyboardButton(text="💻 Informatika-8tabiiy")
    button12 = KeyboardButton(text="🏃 Jismoniy tarbiya-8tabiiy")
    button13 = KeyboardButton(text="🇷🇺 Rus tili-8tabiiy")
    button14 = KeyboardButton(text="🧪 Kimyo-8tabiiy")
    button15 = KeyboardButton(text="🕊️ Tarbiya-8tabiiy")
    button16 = KeyboardButton(text="🤖 Robototexnika-8tabiiy")
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