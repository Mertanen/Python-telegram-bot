from aiogram import Router, F
from aiogram.enums import ParseMode
from aiogram.types import Message, CallbackQuery
from datetime import datetime, timedelta

from formattingSchedule import *
from aiogram_calendar import simple_cal_callback, SimpleCalendar, dialog_cal_callback, DialogCalendar

router = Router()

@router.message(F.text == "Аудитория по дате")
async def cmd(message: Message):
    db = shelve.open('./db/user_data', 'c')
    db[f"st_{message.from_user.id}"] = "CLAS"
    await message.answer("Выберите дату: ", reply_markup=await SimpleCalendar().start_calendar())