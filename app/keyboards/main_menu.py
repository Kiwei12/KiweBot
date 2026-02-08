from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

main_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="🎌 Anime list", callback_data="anime_list")],
        [InlineKeyboardButton(text="🔍 Search anime", callback_data="search_anime")],
        [InlineKeyboardButton(text="❤️ Favorites", callback_data="favorites")],
    ]
)
