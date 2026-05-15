from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def fanozbjahon11():
    button = KeyboardButton(text="🏛 O'zbekiston tarixi-11")
    button2 = KeyboardButton(text="🏛 Jahon tarixi-11")
    button3 = KeyboardButton(text="⏪ Orqaga")

    rkm = ReplyKeyboardMarkup(
        keyboard=[
            [button, button2],
            [button3]
        ],
        resize_keyboard=True)
    return rkm