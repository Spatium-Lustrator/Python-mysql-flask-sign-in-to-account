import mysql.connector

class Requester:

    def make_connection(self):
        conn = mysql.connector.connect(
            user='user',
            password='password',
            host='192.168.0.22',
            database='db',
        )

        return conn

    def return_admin_password(self, login):
        conn = self.make_connection()
        get_query = f"""SELECT password FROM admins WHERE login = '{login}'"""
        with conn.cursor(buffered=True) as cursor:
            cursor.execute(get_query)

        conn.close()
        return cursor.fetchone()[0]
