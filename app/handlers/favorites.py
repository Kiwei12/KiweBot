from aiogram import Router, types
from aiogram.types import CallbackQuery
from app.database.db import DB
from app.keyboards.anime_detail import anime_detail_keyboard

router = Router()

@router.callback_query(lambda c: c.data == "favorites")
async def favorites_handler(callback: CallbackQuery):
    user = DB.fetchone("SELECT * FROM users WHERE telegram_id = ?", (callback.from_user.id,))
    if not user:
        await callback.message.answer("User not found.")
        return
    favs = DB.fetchall("SELECT anime_id FROM favorites WHERE user_id = ?", (user['id'],))
    if not favs:
        await callback.message.answer("No favorites yet.")
        return
    for fav in favs:
        anime = DB.fetchone("SELECT * FROM anime WHERE id = ?", (fav['anime_id'],))
        episodes = DB.fetchall("SELECT * FROM episodes WHERE anime_id = ?", (anime['id'],))
        text = f"<b>{anime['title']}</b>\n{anime['description']}"
        await callback.message.answer_photo(
            anime['poster_file_id'],
            caption=text,
            reply_markup=anime_detail_keyboard(anime['id'], episodes)
        )
