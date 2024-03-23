import sqlite3

class BotDB:

    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

    def user_exists(self, username):
        with self.conn:
            result = self.cursor.execute("SELECT * FROM `user_list` WHERE `username` = ?", (username,))
            return bool(len(result.fetchall()))



    def is_mail_login(self, username):
        with self.conn:
            result = self.cursor.execute("SELECT mail FROM user_list WHERE username = ?", (username,))
            return result.fetchone()[0]
        
    def is_mail_pass(self, username):
        with self.conn:
            result = self.cursor.execute("SELECT password FROM user_list WHERE username = ?", (username,))
            return result.fetchone()[0]



    def user_exists_mail(self, mail):
        with self.conn:
            result = self.cursor.execute("SELECT * FROM `user_list` WHERE `mail` = ?", (mail,))
            return bool(len(result.fetchall()))

    def user_exists_password(self, password):
        with self.conn:
            result = self.cursor.execute("SELECT * FROM `user_list` WHERE `password` = ?", (password,))
            return bool(len(result.fetchall()))

    def get_user_id(self, username):
        result = self.cursor.execute("SELECT `id` FROM `user_list` WHERE `username` = ?", (username,))
        return result.fetchone()[0]
    
    def add_main_user(self, login, mail, password):
        self.cursor.execute("INSERT INTO user_list (username, mail, password) VALUES (?, ?, ?)", (login, mail, password,))
        return self.conn.commit()



    def close(self):
        self.connection.close()
