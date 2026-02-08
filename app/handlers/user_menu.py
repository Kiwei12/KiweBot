from aiogram import Router, types
from aiogram.types import CallbackQuery
from app.database.db import DB
from app.keyboards.anime_detail import anime_detail_keyboard
from app.keyboards.episode_links import episode_links_keyboard

router = Router()

@router.callback_query(lambda c: c.data == "anime_list")
async def anime_list_handler(callback: CallbackQuery):
    animes = DB.fetchall("SELECT * FROM anime")
    if not animes:
        await callback.message.answer("No anime found.")
        return
    for anime in animes:
        episodes = DB.fetchall("SELECT * FROM episodes WHERE anime_id = ?", (anime['id'],))
        text = f"<b>{anime['title']}</b>\n{anime['description']}"
        await callback.message.answer_photo(
            anime['poster_file_id'],
            caption=text,
            reply_markup=anime_detail_keyboard(anime['id'], episodes)
        )

@router.callback_query(lambda c: c.data.startswith("episode_"))
async def episode_handler(callback: CallbackQuery):
    episode_id = int(callback.data.split("_")[1])
    episode = DB.fetchone("SELECT * FROM episodes WHERE id = ?", (episode_id,))
    if episode:
        await callback.message.answer(
            f"Episode {episode['episode_number']}\nChoose:",
            reply_markup=episode_links_keyboard(episode['watch_url'], episode['download_url'])
        )
    else:
        await callback.message.answer("Episode not found.")
