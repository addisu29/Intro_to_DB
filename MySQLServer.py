import mysql.connector

def create_database():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="your_password_here"
        )

        if connection.is_connected():
            cursor = connection.cursor()

            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

            print("Database 'alx_book_store' created successfully!")

            cursor.close()

    except mysql.connector.Error as e:
        print(f"Error connecting to MySQL: {e}")

    finally:
        try:
            if connection.is_connected():
                connection.close()
        except:
            pass


if __name__ == "__main__":
    create_database()