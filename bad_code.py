import sqlite3

def get_user(username):
    # This has a SQL injection bug
    query = "SELECT * FROM users WHERE name = '" + username + "'"
    return query

def slow_function(items):
    # This is slow - it recalculates len() every loop
    total = 0
    i = 0
    while i < len(items):
        total = total + items[i]
        i = i + 1
    return total

password = "admin123"  # Hardcoded password - bad!
