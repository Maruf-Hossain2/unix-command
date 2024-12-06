from flask import Flask, render_template, jsonify
import sqlite3
from command_data import commands_by_category

app = Flask(__name__, template_folder='templates', static_folder='static')

def get_commands_from_db():
    conn = sqlite3.connect('commands.db')
    cursor = conn.cursor()
    all_commands = []

    try:
        for table_name in commands_by_category:
            display_name = table_name.replace('_', ' ').title() # Create display name
            print(f"Querying table: {table_name}, Display Name: {display_name}")
            cursor.execute(f"SELECT * FROM {table_name}")
            rows = cursor.fetchall()
            print(f"Rows fetched from {table_name}: {len(rows)}")
            for row in rows:
                command_data = {
                    'command': row[1],
                    'description': row[2],
                    'syntax': row[3],
                    'example': row[4],
                    'category': display_name # Use the display name here
                }
                all_commands.append(command_data)
    except sqlite3.Error as e:
        print(f"CRITICAL DATABASE ERROR: {e}")
        import traceback
        traceback.print_exc()
        return []
    finally:
        conn.close()
    return all_commands

@app.route('/')
def index():
    print("commands_by_category:", commands_by_category) #Check this first!
    categories = [category.replace('_', ' ').title() for category in commands_by_category.keys()]
    print("Categories:", categories) #Then check this.
    return render_template('index.html', categories=categories)

@app.route('/api/commands')
def api_commands():
    return jsonify(get_commands_from_db())
if __name__ == '__main__':
    app.run(debug=True)