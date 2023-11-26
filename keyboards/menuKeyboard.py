from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def getMenuKeyboard():
    keyboard = [
        [
            KeyboardButton(text='Расписание на сегодня'),
            KeyboardButton(text='Расписание на завтра')
        ],
        [
            KeyboardButton(text= "Выбрать дату"),
            KeyboardButton(text='Экзамены')
        ],
        [
            KeyboardButton(text='Выбрать расписание')
        ]
        
    ]
    menuKeyboard = ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)
    return menuKeyboard

