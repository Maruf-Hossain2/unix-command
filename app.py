from flask import Flask, render_template, jsonify, request
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
    categories = [category.replace('_', ' ').title() for category in commands_by_category.keys()]
    return render_template('index.html', categories=categories)

@app.route('/api/search', methods=['GET'])
def search_commands():
    from flask import request
    query = request.args.get('q', '').strip().lower()
    if not query:
        return jsonify([])  # Return empty list if no query is provided
    
    conn = sqlite3.connect('commands.db')
    cursor = conn.cursor()
    search_results = {}

    try:
        for table_name in commands_by_category:
            cursor.execute(f"""
                SELECT command, description, syntax, example
                FROM {table_name}
                WHERE command LIKE ? OR description LIKE ?
            """, (f'%{query}%', f'%{query}%'))
            rows = cursor.fetchall()
            if rows:
                display_name = table_name.replace('_', ' ').title()
                if display_name not in search_results:
                    search_results[display_name] = []
                for row in rows:
                    search_results[display_name].append({
                        'command': row[0],
                        'description': row[1],
                        'syntax': row[2],
                        'example': row[3]
                    })
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        conn.close()
    
    return jsonify(search_results)

@app.route('/api/commands')
def api_commands():
    return jsonify(get_commands_from_db())
if __name__ == '__main__':
    app.run(debug=True)