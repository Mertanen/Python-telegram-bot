from datetime import timedelta
from aiogram import Router, F
from aiogram.enums import ParseMode
from aiogram.types import Message, CallbackQuery

from formattingSchedule import *
from aiogram_calendar import simple_cal_callback, SimpleCalendar, dialog_cal_callback, DialogCalendar
from keyboards.scheduleMenuKeyboard import getMenuChooseKeyboard

router = Router()

@router.message(F.text == "Расписание на сегодня")
async def menu(message: Message):
    schedule = getScheduleOnDate(user_id=message.from_user.id, date=datetime.now())
    await message.answer(schedule, parse_mode=ParseMode.HTML)
    

            
@router.message(F.text == "Расписание на завтра")
async def menu(message: Message):
    schedule = getScheduleOnDate(user_id=message.from_user.id, date=datetime.now() + timedelta(days=1))
    await message.answer(schedule, parse_mode=ParseMode.HTML)
    
@router.message(F.text == "Выбрать дату")
async def menu(message: Message):
    db = shelve.open('./db/user_data', 'c')
    db[f"st_{message.from_user.id}"] = "MENU"
    await message.answer("Выберите дату: ", reply_markup=await SimpleCalendar().start_calendar())
    
@router.message(F.text == "Экзамены")
async def menu(message: Message):
    schedule = getScheduleExams(user_id=message.from_user.id)
    await message.answer(schedule, parse_mode=ParseMode.HTML)
    
@router.message(F.text == "Выбрать расписание")
async def menu(message: Message):
    await message.answer(text="Выберите пункт", reply_markup=getMenuChooseKeyboard())

@router.callback_query(simple_cal_callback.filter())
async def process_simple_calendar(callback_query: CallbackQuery, callback_data: dict):
    selected, date = await SimpleCalendar().process_selection(callback_query, callback_data)
    db = shelve.open('./db/user_data', 'c')
    if selected:
        if db[f'st_{callback_query.from_user.id}'] == "MENU":
            schedule = getScheduleOnDate(callback_query.from_user.id, date)
            await callback_query.message.answer(
                f'{schedule}',
                parse_mode=ParseMode.HTML
            )
            del db[f'st_{callback_query.from_user.id}']
            db.close()
            
        elif db[f'st_{callback_query.from_user.id}'] == "PROF":
            schedule = getProfessorDaySchedule(callback_query.from_user.id, date)
            await callback_query.message.answer(
                f'{schedule}',
                parse_mode=ParseMode.HTML
            ) 
            del db[f'st_{callback_query.from_user.id}']
            db.close()
            
        elif db[f'st_{callback_query.from_user.id}'] == "CLAS":
            schedule = getClassroomOnDate(callback_query.from_user.id, date)
            await callback_query.message.answer(
                f'{schedule}',
                parse_mode=ParseMode.HTML
            )
            del db[f'st_{callback_query.from_user.id}']
            db.close()
        