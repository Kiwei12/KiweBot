from aiogram import Router, types
from aiogram.types import CallbackQuery
from app.keyboards.admin_menu import admin_menu
from app.utils.env import ADMIN_ID

router = Router()

@router.callback_query(lambda c: c.from_user.id == ADMIN_ID and c.data == "admin_panel")
async def admin_panel_handler(callback: CallbackQuery):
    await callback.message.answer("Admin Panel:", reply_markup=admin_menu)
