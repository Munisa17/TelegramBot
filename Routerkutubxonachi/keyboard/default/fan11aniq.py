from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def fan11aniq():
    button = KeyboardButton(text="📖 Ona tili-11aniq")
    button2 = KeyboardButton(text="📘 Adabiyot-11aniq")
    button3 = KeyboardButton(text="🔢 Algebra-11aniq")
    button4 = KeyboardButton(text="📐 Geometriya-11aniq")
    button5 = KeyboardButton(text="🏛 Tarix(O'zbekiston va jahon tarixi)-11aniq")
    button6 = KeyboardButton(text="🗣 Ingliz tili-11aniq")
    button7 = KeyboardButton(text="⚛️ Fizika-11aniq")
    button8 = KeyboardButton(text="🌱 Biologiya-11aniq")
    button9 = KeyboardButton(text="💻 Informatika-11aniq")
    button10 = KeyboardButton(text="🏃 Jismoniy tarbiya-11aniq")
    button11 = KeyboardButton(text="🇷🇺 Rus tili-11aniq")
    button12 = KeyboardButton(text="🧪 Kimyo-11aniq")
    button13 = KeyboardButton(text="🕊️ Tarbiya-11aniq")
    button14 = KeyboardButton(text="🪖 Chaqiruvga qadar boshlang'ich tayyorgarlik-11aniq")
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