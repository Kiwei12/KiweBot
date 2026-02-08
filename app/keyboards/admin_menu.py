from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

admin_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="➕ Add anime", callback_data="admin_add_anime")],
        [InlineKeyboardButton(text="✏️ Edit anime", callback_data="admin_edit_anime")],
        [InlineKeyboardButton(text="❌ Delete anime", callback_data="admin_delete_anime")],
        [InlineKeyboardButton(text="➕ Add episodes", callback_data="admin_add_episodes")],
        [InlineKeyboardButton(text="📢 Broadcast message", callback_data="admin_broadcast")],
    ]
)
