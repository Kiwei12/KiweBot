from aiogram import Router, types
from aiogram.types import CallbackQuery
from app.database.db import DB
from app.keyboards.anime_detail import anime_detail_keyboard

router = Router()

@router.callback_query(lambda c: c.data == "search_anime")
async def search_anime_handler(callback: CallbackQuery):
    await callback.message.answer("Send anime title to search:")

@router.message()
async def search_text_handler(message: types.Message):
    if not hasattr(message, 'reply_to_message') or not message.reply_to_message:
        return
    if message.reply_to_message.text != "Send anime title to search:":
        return
    title = message.text.strip()
    animes = DB.fetchall("SELECT * FROM anime WHERE title LIKE ?", (f"%{title}%",))
    if not animes:
        await message.answer("No anime found.")
        return
    for anime in animes:
        episodes = DB.fetchall("SELECT * FROM episodes WHERE anime_id = ?", (anime['id'],))
        text = f"<b>{anime['title']}</b>\n{anime['description']}"
        await message.answer_photo(
            anime['poster_file_id'],
            caption=text,
            reply_markup=anime_detail_keyboard(anime['id'], episodes)
        )
