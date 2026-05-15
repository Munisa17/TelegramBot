from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def fananiqtabiiy8():
    button = KeyboardButton(text="📘 aniq fanlar-8")
    button2 = KeyboardButton(text="🧬 tabiiy fanlar-8")
    button3 = KeyboardButton(text="⏪ Orqaga")

    rkm = ReplyKeyboardMarkup(
        keyboard=[
            [button,button2],
            [button3]
        ],
        resize_keyboard=True)
    return rkm