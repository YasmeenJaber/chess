import pandas as pd
import sqlite3

# قراءة ملف CSV
df = pd.read_csv('data/raw/chess_games.csv')

# إنشاء قاعدة البيانات
conn = sqlite3.connect('data/chess.db')

# إنشاء جدول games
df.to_sql('games', conn, if_exists='replace', index=False)

print("Database created successfully!")

# قراءة ملف اللاعبين
df_players = pd.read_csv('data/raw/player_registry.csv')

# إضافة جدول اللاعبين إلى نفس قاعدة البيانات
df_players.to_sql('players_registry', conn, if_exists='replace', index=False)

print("Players table added successfully!")

conn.close()