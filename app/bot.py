import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand
from app.utils.env import BOT_TOKEN
from app.handlers.start import router as start_router
from app.handlers.user_menu import router as user_menu_router
from app.handlers.search import router as search_router
from app.handlers.favorites import router as favorites_router
from app.admin.panel import router as admin_panel_router
from app.admin.add_anime import router as add_anime_router
from app.admin.edit_anime import router as edit_anime_router
from app.admin.delete_anime import router as delete_anime_router
from app.admin.add_episodes import router as add_episodes_router
from app.admin.broadcast import router as broadcast_router
from app.middlewares.admin_check import AdminCheckMiddleware
from loguru import logger

async def main():
    bot = Bot(token=BOT_TOKEN, parse_mode="HTML")
    dp = Dispatcher()

    # Register routers
    dp.include_router(start_router)
    dp.include_router(user_menu_router)
    dp.include_router(search_router)
    dp.include_router(favorites_router)
    dp.include_router(admin_panel_router)
    dp.include_router(add_anime_router)
    dp.include_router(edit_anime_router)
    dp.include_router(delete_anime_router)
    dp.include_router(add_episodes_router)
    dp.include_router(broadcast_router)

    # Register admin middleware
    dp.message.middleware(AdminCheckMiddleware())
    dp.callback_query.middleware(AdminCheckMiddleware())

    # Set bot commands
    await bot.set_my_commands([
        BotCommand(command="start", description="Start bot")
    ])

    logger.info("Bot started.")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
