"""
Author: Abdullah Shahzad
Created on: Aug 29, 2024

Task:
- Perform crud operation
"""

import psycopg2


class Wrapper:
    """
    A wrapper class for managing PostgresSQL database connections and operations.
    """

    def __init__(self, port, dbname, user, password):
        """
        Initializes the database connection parameters.

        @param port: Port number to connect to the database. (int)
        @param dbname: The name of the database. (string)
        @param user: The database user. (string)
        @param password: The user's password. (string)
        """
        self.host = "localhost"
        self.dbname = dbname
        self.port = port
        self.user = user
        self.password = password
        self.conn = None
        self.cur = None

    def connect_table(self):
        """
        Establishes a connection to the PostgreSQL database.
        """
        try:
            self.conn = psycopg2.connect(
                host=self.host,
                dbname=self.dbname,
                user=self.user,
                password=self.password,
                port=self.port
            )
            self.cur = self.conn.cursor()
            print("Connection successful")
        except Exception as e:
            print(f"Failed to connect: {e}")

    def create_table(self):
        """
        Creates a 'person' table and inserts records into it if it does not already exist.
        """
        try:
            self.cur.execute("""
                CREATE TABLE IF NOT EXISTS person(
                    id INT PRIMARY KEY,
                    age INT,
                    name VARCHAR(100),
                    gender CHAR(1)
                );
            """)

            self.cur.execute("""
                INSERT INTO person (id, age, name, gender)
                VALUES 
                    (1, 30, 'Mike', 'M'),
                    (2, 28, 'John', 'M'),
                    (3, 25, 'Lisa', 'F'),
                    (4, 33, 'Bob', 'M')
            """)

            self.conn.commit()
            print("Table created and records inserted successfully")
        except Exception as e:
            print(f"Error in creating table: {e}")

    def update_table(self):
        """
        Updates a record in the 'person' table based on user input for ID and new name.
        """
        try:
            # Get input from the user
            id = int(input("Enter the ID of the person to update: "))
            new_name = input("Enter the new name: ")

            # Execute update query
            self.cur.execute("""
                UPDATE person
                SET name = %s
                WHERE id = %s
            """, (new_name, id))

            self.conn.commit()

            updated_rows = self.cur.rowcount
            if updated_rows:
                print(f"Record updated successfully, {updated_rows} row(s) affected")
            else:
                print("No record found with the specified ID")

        except Exception as e:
            print(f"Error in updating table: {e}")
        except ValueError:
            print("Invalid input. Please enter a valid ID.")

    def delete_table(self):
        """
        Deletes the 'person' table from the database.
        """
        try:
            self.cur.execute("DROP TABLE IF EXISTS person")
            self.conn.commit()
            print("Table deleted successfully")
        except Exception as e:
            print(f"Error in deleting table: {e}")

    def view_table(self):
        """
        Displays all records from the 'person' table.
        """
        try:
            self.cur.execute("SELECT * FROM person")
            rows = self.cur.fetchall()

            if rows:
                print("ID | Age | Name | Gender")
                print("-" * 30)
                for row in rows:
                    print(f"{row[0]} | {row[1]} | {row[2]} | {row[3]}")
            else:
                print("No records found.")
        except Exception as e:
            print(f"Error in viewing table: {e}")

    def close_connection(self):
        """
        Closes the database connection and cursor.
        """
        if self.cur:
            self.cur.close()
        if self.conn:
            self.conn.close()
        print("Connection closed")


if __name__ == '__main__':
    obj1 = Wrapper(port=5433, dbname="postgres", user="postgres", password="1499")
    obj1.connect_table()

    while True:
        print("\nMenu:")
        print("1. Create Table and Insert Records")
        print("2. Update Table Record")
        print("3. Delete Table")
        print("4. View Table")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            obj1.create_table()
        elif choice == '2':
            obj1.update_table()
        elif choice == '3':
            obj1.delete_table()
        elif choice == '4':
            obj1.view_table()
        elif choice == '5':
            print("Exiting...")
            obj1.close_connection()
            break
        else:
            print("Invalid choice, please try again.")
