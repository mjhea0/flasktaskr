from views import db
from _config import DATABASE_PATH

import sqlite3
from datetime import datetime

with sqlite3.connect(DATABASE_PATH) as connection:

    c = connection.cursor()

    c.execute("""ALTER TABLE tasks RENAME TO old_tasks""")

    db.create_all()

    c.execute("""SELECT name, due_date, priority,
              status FROM old_tasks ORDER BY task_id ASC""")

    data = [(row[0], row[1], row[2], row[3],
            datetime.now(), 1) for row in c.fetchall()]

    c.executemany("""INSERT INTO tasks (name, due_date, prioirity, status,
                  posted_date, user_id) VALUES (?, ?, ?, ?, ?, ?)""", data)

    c.execute("DROP TABLE old_tasks")
