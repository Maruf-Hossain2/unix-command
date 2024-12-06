import sqlite3
from command_data import commands_by_category

conn = sqlite3.connect('commands.db')
cursor = conn.cursor()

for category, commands_list in commands_by_category.items():
    cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS {category} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            command TEXT UNIQUE,
            description TEXT,
            syntax TEXT,
            example TEXT
        )
    ''')
    cursor.executemany(f"INSERT OR IGNORE INTO {category} (command, description, syntax, example) VALUES (?, ?, ?, ?)", commands_list)

conn.commit()
conn.close()

print("Database populated successfully!")
