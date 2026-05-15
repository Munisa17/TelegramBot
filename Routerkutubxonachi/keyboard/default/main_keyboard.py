from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def menu():
    button = KeyboardButton(text="📚 5-sinf")
    button2 = KeyboardButton(text="📘 6-sinf")
    button3 = KeyboardButton(text="📗 7-sinf")
    button4 = KeyboardButton(text="📙 8-sinf")
    button5 = KeyboardButton(text ="📖 9-sinf")
    button6 = KeyboardButton(text="🎓 10-sinf")
    button7 = KeyboardButton(text="🏆 11-sinf")

    rkm = ReplyKeyboardMarkup(
        keyboard=[
            [button,button2],
            [button3, button4],
            [button5],[button6],
            [button7]
        ],
        resize_keyboard=True)
    return rkm