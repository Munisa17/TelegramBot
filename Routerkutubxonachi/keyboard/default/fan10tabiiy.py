from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def fan10tabiiy():
    button = KeyboardButton(text="📖 Ona tili-10tabiiy")
    button2 = KeyboardButton(text="📘 Adabiyot-10tabiiy")
    button3 = KeyboardButton(text="🔢 Algebra-10tabiiy")
    button4 = KeyboardButton(text="📐 Geometriya-10tabiiy")
    button5 = KeyboardButton(text="🏛 Tarix(O'zbekiston va jahon tarixi)-10tabiiy")
    button6 = KeyboardButton(text="🗣 Ingliz tili-10tabiiy")
    button7 = KeyboardButton(text="⚛️ Fizika-10tabiiy")
    button8 = KeyboardButton(text="🌱 Biologiya-10tabiiy")
    button9 = KeyboardButton(text="💻 Informatika-10tabiiy")
    button10 = KeyboardButton(text="🏃 Jismoniy tarbiya-10tabiiy")
    button11 = KeyboardButton(text="🇷🇺 Rus tili-10tabiiy")
    button12 = KeyboardButton(text="🧪 Kimyo-10tabiiy")
    button13 = KeyboardButton(text="🕊️ Tarbiya-10tabiiy")
    button14 = KeyboardButton(text="🪖 Chaqiruvga qadar boshlang'ich tayyorgarlik-10tabiiy")
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