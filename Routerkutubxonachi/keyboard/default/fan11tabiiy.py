from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def fan11tabiiy():
    button = KeyboardButton(text="📖 Ona tili-11tabiiy")
    button2 = KeyboardButton(text="📘 Adabiyot-11tabiiy")
    button3 = KeyboardButton(text="🔢 Algebra-11tabiiy")
    button4 = KeyboardButton(text="📐 Geometriya-11tabiiy")
    button5 = KeyboardButton(text="🏛 Tarix(O'zbekiston va jahon tarixi)-11tabiiy")
    button6 = KeyboardButton(text="🗣 Ingliz tili-11tabiiy")
    button7 = KeyboardButton(text="⚛️ Fizika-11tabiiy")
    button8 = KeyboardButton(text="🌱 Biologiya-11tabiiy")
    button9 = KeyboardButton(text="💻 Informatika-11tabiiy")
    button10 = KeyboardButton(text="🏃 Jismoniy tarbiya-11tabiiy")
    button11 = KeyboardButton(text="🇷🇺 Rus tili-11tabiiy")
    button12 = KeyboardButton(text="🧪 Kimyo-11tabiiy")
    button13 = KeyboardButton(text="🕊️ Tarbiya-11tabiiy")
    button14 = KeyboardButton(text="🪖 Chaqiruvga qadar boshlang'ich tayyorgarlik-11tabiiy")
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