from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

def getMenuChooseKeyboard():
    keyboard = [
        [
            KeyboardButton(text='Расписание на эту неделю'),   
        ],
        [
          KeyboardButton(text='Расписание на следующую неделю')  
        ],
        [
            KeyboardButton(text='Расписание преподавателя'),
            KeyboardButton(text='Расписание аудитории')
        ],

        [
            KeyboardButton(text='Меню')
        ]     
    ]
    menuChooseKeyboard = ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)
    return menuChooseKeyboard

def professorReplyKeyboard():
    keyboard = [
        [
            KeyboardButton(text='На сегодня'),
            KeyboardButton(text='На эту неделю')
        ],
        [
            KeyboardButton(text='На следующую неделю'),
            KeyboardButton(text='По дате')
        ],
        [
            KeyboardButton(text='Меню расписания')
        ]     
    ]
    menuChooseKeyboard = ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)
    return menuChooseKeyboard

def classroomReplyKeyboard():
    keyboard = [
        [
            KeyboardButton(text='Аудитория по дате'),
        ],
        [
            KeyboardButton(text='Меню расписания')
        ]     
    ]
    menuChooseKeyboard = ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)
    return menuChooseKeyboard