from aiogram.types import Message, InlineKeyboardButton, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder

from Scheduler import Scheduler

################### On start ##################

def facultyKeybouard(data: Scheduler):
    schedule = data.getfacultyDictionary()
    builder = InlineKeyboardBuilder()
    for item in schedule.keys():
        builder.add(InlineKeyboardButton(
            text=f"{item}",
            callback_data=f"f_{item}"
        ))
    builder.adjust(4)
    return builder

def courseKeybouard(data: Scheduler):
    data.courseList()
    schedule = data.getCourseList()
    builder = InlineKeyboardBuilder()
    for item in schedule:
        builder.add(InlineKeyboardButton(
            text=f"{item}",
            callback_data=f"c_{item}"
        ))
    builder.adjust(2)
    return builder

def groupKeyboard(data: Scheduler):
    data.groupDict()
    schedule = data.getGroup()
    builder = InlineKeyboardBuilder()
    for item in schedule.keys():
        builder.add(InlineKeyboardButton(
            text=f"{item}",
            callback_data=f"g_{item}"
        ))
    builder.adjust(4)
    return builder

####################### Professor #####################

def DivisionKeybouard(data: Scheduler):
    schedule = data.getfacultyDictionary()
    if "Асп" in schedule:
        del schedule["Асп"]
    if "Ординатура" in schedule:
        del schedule["Ординатура"]
    builder = InlineKeyboardBuilder()
    for item in schedule.keys():
        builder.add(InlineKeyboardButton(
            text=f"{item}",
            callback_data=f"d_{item}"
        ))
    builder.adjust(4)
    return builder

def kafedraKeybouard(data: Scheduler):
    data.kafedra()
    schedule = data.getKafedra()
    builder = InlineKeyboardBuilder()
    for item in schedule.keys():
        builder.add(InlineKeyboardButton(
            text=f"{item}",
            callback_data=f"k_{item}"
        ))
    builder.adjust(3)
    return builder

def professorKeyboard(data: Scheduler):
    data.professor()
    schedule = data.getProfessorList()
    builder = InlineKeyboardBuilder()
    for item in schedule.keys():
        builder.add(InlineKeyboardButton(
            text=f"{item}",
            callback_data=f"p_{item}"
        )) 
    builder.adjust(2)
    return builder

################### Classroom ###################

def korpusKeybouard(data: Scheduler):
    schedule = data.getKorpusList()
    builder = InlineKeyboardBuilder()
    row1 = []
    for item in schedule[:-1]:
        row1.append(InlineKeyboardButton(
            text=f"{item}",
            callback_data=f"kp_{item}"
        ))   
    row2 = []
    row2.append(InlineKeyboardButton(
        text=f"Фундаментальная библиотека",
        callback_data=f"kp_{schedule[-1]}"
    ))
    
    builder.row(*row1, width=5)
    builder.row(*row2)
    
    return builder

def classroomKeybouard(data: Scheduler):
    data.classromList()
    schedule = data.getClassromList()
    builder = InlineKeyboardBuilder()
    for item in schedule:
        builder.add(InlineKeyboardButton(
            text=f"{item}",
            callback_data=f"cl_{item}"
        ))
    builder.adjust(6)
    return builder