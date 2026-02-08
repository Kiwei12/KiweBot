from aiogram import Router, types
from aiogram.filters import Command
from app.keyboards.main_menu import main_menu
from app.database.db import DB
from app.utils.logger import logger

router = Router()

@router.message(Command("start"))
async def start_handler(message: types.Message):
    user = DB.fetchone("SELECT * FROM users WHERE telegram_id = ?", (message.from_user.id,))
    if not user:
        DB.execute("INSERT INTO users (telegram_id, username) VALUES (?, ?)", (message.from_user.id, message.from_user.username))
        logger.info(f"New user: {message.from_user.id} ({message.from_user.username})")
    await message.answer(
        "👋 Welcome to the Anime Bot!\nChoose an option:",
        reply_markup=main_menu
    )
