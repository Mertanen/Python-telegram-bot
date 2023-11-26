from aiogram import Router, F
from aiogram.enums import ParseMode
from aiogram.types import Message, CallbackQuery
from datetime import datetime, timedelta

from formattingSchedule import *
from aiogram_calendar import simple_cal_callback, SimpleCalendar, dialog_cal_callback, DialogCalendar

router = Router()

@router.message(F.text == "На сегодня")
async def cmd(message: Message):
    schedule = getProfessorDaySchedule(user_id=message.from_user.id, date=datetime.now())
    await message.answer(text=schedule, parse_mode=ParseMode.HTML)
    
@router.message(F.text == "На эту неделю")
async def cmd(message: Message):
    schedule = getProfessorWeekSchedule(user_id=message.from_user.id, date=datetime.now())
    await message.answer(text=schedule, parse_mode=ParseMode.HTML)

@router.message(F.text == "На следующую неделю")
async def cmd(message: Message):
    schedule = getProfessorWeekSchedule(user_id=message.from_user.id, date=datetime.now() + timedelta(days=7))
    await message.answer(text=schedule, parse_mode=ParseMode.HTML)

@router.message(F.text == "По дате")
async def cmd(message: Message):
    db = shelve.open('./db/user_data', 'c')
    db[f"st_{message.from_user.id}"] = "PROF"
    await message.answer("Выберите дату: ", reply_markup=await SimpleCalendar().start_calendar())
    