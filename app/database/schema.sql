-- SQLite schema for Telegram Anime Bot

CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    telegram_id INTEGER UNIQUE NOT NULL,
    username TEXT
);

CREATE TABLE IF NOT EXISTS anime (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    poster_file_id TEXT
);

CREATE TABLE IF NOT EXISTS episodes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    anime_id INTEGER NOT NULL,
    episode_number INTEGER NOT NULL,
    watch_url TEXT,
    download_url TEXT,
    FOREIGN KEY (anime_id) REFERENCES anime(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS favorites (
    user_id INTEGER NOT NULL,
    anime_id INTEGER NOT NULL,
    PRIMARY KEY (user_id, anime_id),
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (anime_id) REFERENCES anime(id) ON DELETE CASCADE
);
