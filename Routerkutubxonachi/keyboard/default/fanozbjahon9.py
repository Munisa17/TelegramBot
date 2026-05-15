from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def fanozbjahon9():
    button = KeyboardButton(text="🏛 O'zbekiston tarixi-9")
    button2 = KeyboardButton(text="🏛 Jahon tarixi-9")
    button3 = KeyboardButton(text="⏪ Orqaga")

    rkm = ReplyKeyboardMarkup(
        keyboard=[
            [button, button2],
            [button3]
        ],
        resize_keyboard=True)
    return rkm