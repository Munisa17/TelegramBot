from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def fananiqtabiiy7():
    button = KeyboardButton(text="📘 aniq fanlar-7")
    button2 = KeyboardButton(text="🧬 tabiiy fanlar-7")
    button3 = KeyboardButton(text="⏪ Orqaga")

    rkm = ReplyKeyboardMarkup(
        keyboard=[
            [button,button2],
            [button3]
        ],
        resize_keyboard=True)
    return rkm