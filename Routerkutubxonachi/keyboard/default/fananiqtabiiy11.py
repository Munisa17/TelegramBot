from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def fananiqtabiiy11():
    button = KeyboardButton(text="📘 aniq fanlar-11")
    button2 = KeyboardButton(text="🧬 tabiiy fanlar-11")
    button3 = KeyboardButton(text="⏪ Orqaga")

    rkm = ReplyKeyboardMarkup(
        keyboard=[
            [button,button2],
            [button3]
        ],
        resize_keyboard=True)
    return rkm