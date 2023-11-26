# flake8: noqa
"""
Simple Inline Calendar & Date Selection tool for Aiogram (version 3.0.0b6 and upper) Telegram bots
"""
__version__ = '0.1.2'
import aiogram_calendar.calendar as calendar
from aiogram import __version__ as __aiogram_version__
assert __aiogram_version__.split('.', maxsplit=1)[0] == '3', \
    'Current module requires aiogram package version 3.x.x'

from aiogram_calendar.simple_calendar \
    import SimpleCalendarCallback as simple_cal_callback, SimpleCalendar
from aiogram_calendar.dialog_calendar \
    import DialogCalendarCallback as dialog_cal_callback, DialogCalendar
