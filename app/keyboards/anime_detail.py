from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def anime_detail_keyboard(anime_id, episodes):
    buttons = []
    for ep in episodes:
        buttons.append([
            InlineKeyboardButton(
                text=f"Episode {ep['episode_number']}",
                callback_data=f"episode_{ep['id']}"
            )
        ])
    return InlineKeyboardMarkup(inline_keyboard=buttons)
