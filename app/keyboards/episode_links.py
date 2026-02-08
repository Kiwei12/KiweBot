from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def episode_links_keyboard(watch_url, download_url):
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="📺 Watch", url=watch_url)],
            [InlineKeyboardButton(text="⬇️ Download", url=download_url)]
        ]
    )
