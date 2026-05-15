from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def fanozbjahon8():
    button = KeyboardButton(text="🏛 O'zbekiston tarixi-8")
    button2 = KeyboardButton(text="🏛 Jahon tarixi-8")
    button3 = KeyboardButton(text="⏪ Orqaga")

    rkm = ReplyKeyboardMarkup(
        keyboard=[
            [button, button2],
            [button3]
        ],
        resize_keyboard=True)
    return rkm