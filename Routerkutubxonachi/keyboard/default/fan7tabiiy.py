from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def fan7tabiiy():
    button = KeyboardButton(text="📖 Ona tili-7tabiiy")
    button2 = KeyboardButton(text="📘 Adabiyot-7tabiiy")
    button3 = KeyboardButton(text="🔢 Algebra-7tabiiy")
    button4 = KeyboardButton(text="📐 Geometriya7tabiiy")
    button5 = KeyboardButton(text="🌍 Geografiya-7tabiiy")
    button6 = KeyboardButton(text="🏛 Tarix(O'zbekiston va jahon tarixi)-7tabiiy")
    button7 = KeyboardButton(text="🗣 Ingliz tili-7tabiiy")
    button8 = KeyboardButton(text="⚛️ Fizika-7tabiiy")
    button9 = KeyboardButton(text="🌱 Biologiya-7tabiiy")
    button10 = KeyboardButton(text="🎨 ART-7tabiiy")
    button11 = KeyboardButton(text="💻 Informatika-7tabiiy")
    button12 = KeyboardButton(text="🏃 Jismoniy tarbiya-7tabiiy")
    button13 = KeyboardButton(text="🇷🇺 Rus tili-7tabiiy")
    button14 = KeyboardButton(text="🧪 Kimyo-7tabiiy")
    button15 = KeyboardButton(text="🕊️ Tarbiya-7tabiiy")
    button16 = KeyboardButton(text="🤖 Robototexnika-7tabiiy")
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