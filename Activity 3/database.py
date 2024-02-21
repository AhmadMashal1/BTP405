import psycopg2

class Database:
    def __init__(self):
        # Connect to the PostgreSQL database
        self.connection = psycopg2.connect(
            dbname='notes',
            user='root',
            password='password',
            host='db',
            port='5432'
        )

        # Create notes table if it doesn't exist
        with self.connection.cursor() as cursor:
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS notes (
                id SERIAL PRIMARY KEY,
                title VARCHAR(255) NOT NULL,
                content TEXT
            )
            """)
            self.connection.commit()

    def create_note(self, title, content):
        # Insert a new note into the database
        with self.connection.cursor() as cursor:
            sql = "INSERT INTO notes (title, content) VALUES (%s, %s)"
            cursor.execute(sql, (title, content))
            self.connection.commit()
            return cursor.lastrowid

    def read_notes(self):
        # Retrieve all notes from the database
        with self.connection.cursor() as cursor:
            cursor.execute("SELECT * FROM notes")
            return cursor.fetchall()

    def read_note(self, note_id):
        # Retrieve a specific note from the database by ID
        with self.connection.cursor() as cursor:
            sql = "SELECT * FROM notes WHERE id = %s"
            cursor.execute(sql, (note_id,))
            return cursor.fetchone()

    def update_note(self, note_id, title, content):
        # Update a note in the database
        with self.connection.cursor() as cursor:
            sql = "UPDATE notes SET title = %s, content = %s WHERE id = %s"
            cursor.execute(sql, (title, content, note_id))
            self.connection.commit()

    def delete_note(self, note_id):
        # Delete a note from the database by ID
        with self.connection.cursor() as cursor:
            sql = "DELETE FROM notes WHERE id = %s"
            cursor.execute(sql, (note_id,))
            self.connection.commit()

    def close_connection(self):
        # Close the database connection
        self.connection.close()
