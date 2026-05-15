from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def fan10aniq():
    button = KeyboardButton(text="📖 Ona tili-10aniq")
    button2 = KeyboardButton(text="📘 Adabiyot-10aniq")
    button3 = KeyboardButton(text="🔢 Algebra-10aniq")
    button4 = KeyboardButton(text="📐 Geometriya-10aniq")
    button5 = KeyboardButton(text="🏛 Tarix(O'zbekiston va jahon tarixi)-10aniq")
    button6 = KeyboardButton(text="🗣 Ingliz tili-10aniq")
    button7 = KeyboardButton(text="⚛️ Fizika-10aniq")
    button8 = KeyboardButton(text="🌱 Biologiya-10aniq")
    button9 = KeyboardButton(text="💻 Informatika-10aniq")
    button10 = KeyboardButton(text="🏃 Jismoniy tarbiya-10aniq")
    button11 = KeyboardButton(text="🇷🇺 Rus tili-10aniq")
    button12 = KeyboardButton(text="🧪 Kimyo-10aniq")
    button13 = KeyboardButton(text="🕊️ Tarbiya-10aniq")
    button14 = KeyboardButton(text="🪖 Chaqiruvga qadar boshlang'ich tayyorgarlik-10aniq")
    button15 = KeyboardButton(text="⏪ Orqaga")

    rkm = ReplyKeyboardMarkup(
        keyboard=[
            [button, button2, button3],
            [button4, button5, button6],
            [button7, button8, button9],
            [button10, button11, button12],
            [button13, button14],
            [button15]
        ],
        resize_keyboard=True)
    return rkm