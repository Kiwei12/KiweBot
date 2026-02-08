from aiogram import BaseMiddleware
from aiogram.types import Message, CallbackQuery
from app.utils.env import ADMIN_ID

class AdminCheckMiddleware(BaseMiddleware):
    async def __call__(self, handler, event, data):
        user_id = None
        if isinstance(event, Message):
            user_id = event.from_user.id
        elif isinstance(event, CallbackQuery):
            user_id = event.from_user.id
        if user_id == ADMIN_ID:
            return await handler(event, data)
        else:
            if isinstance(event, Message):
                await event.answer("You are not admin.")
            elif isinstance(event, CallbackQuery):
                await event.answer("You are not admin.", show_alert=True)
            return
