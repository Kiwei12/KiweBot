# Telegram Anime Bot

A production-ready Telegram Anime Bot built with Python and aiogram, using SQLite for storage. Compatible with Railway hosting (long polling, no webhook).

## Features
- /start command with welcome message
- Inline keyboard main menu: Anime list, Search anime, Favorites
- Anime detail page: poster, description, episode buttons
- Episode links: watch/download
- Admin panel (admin only): add/edit/delete anime, add episodes, broadcast message
- Step-by-step admin flows
- SQLite database (local file)
- Async/await, error handling, logging

## Folder Structure
```
app/
  bot.py
  __init__.py
  database/
    db.py
    schema.sql
  handlers/
    start.py
    user_menu.py
    search.py
    favorites.py
  keyboards/
    main_menu.py
    admin_menu.py
    anime_detail.py
    episode_links.py
  utils/
    logger.py
    env.py
  middlewares/
    admin_check.py
  admin/
    panel.py
    add_anime.py
    edit_anime.py
    delete_anime.py
    add_episodes.py
    broadcast.py
.env.example
requirements.txt
README.md
```

## SQLite Schema
See `app/database/schema.sql` for full schema.

## Railway Deployment Instructions
1. Fork/clone this repo.
2. Add your bot token and admin ID to Railway environment variables:
   - `BOT_TOKEN`
   - `ADMIN_ID`
3. Railway start command:
   ```
   python app/bot.py
   ```
4. Deploy. Railway will install dependencies from `requirements.txt` and run the bot.

## Example .env
```
BOT_TOKEN=your_bot_token_here
ADMIN_ID=123456789
```

## Requirements
See `requirements.txt`.

## Notes
- No external databases (Supabase, etc.)
- No webhooks (uses long polling)
- All admin flows are step-by-step and handled in bot logic
- Poster images are stored as Telegram file_id

## License
MIT
