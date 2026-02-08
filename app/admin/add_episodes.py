from aiogram import Router, types
from aiogram.types import CallbackQuery
from app.database.db import DB
from app.utils.env import ADMIN_ID

router = Router()

@router.callback_query(lambda c: c.from_user.id == ADMIN_ID and c.data == "admin_add_episodes")
async def admin_add_episodes_handler(callback: CallbackQuery):
    await callback.message.answer("Send anime ID to add episodes:")
    # Step-by-step flow will be handled in main bot file
