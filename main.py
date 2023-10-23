import mysql.connector

# Connect to MySQL
db = mysql.connector.connect(
    host="your_mysql_host",
    user="your_mysql_user",
    password="your_mysql_password",
    database="your_database_name"
)

cursor = db.cursor()

# Create users table if not exists
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(255) UNIQUE,
        password VARCHAR(255)
    )
""")

def signup():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Check if username already exists
    cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
    existing_user = cursor.fetchone()

    if existing_user:
        print("Username already exists. Please choose another.")
    else:
        # Insert new user into the database
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
        db.commit()
        print("Signup successful!")

def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Check if the entered credentials are valid
    cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
    matched_user = cursor.fetchone()

    if matched_user:
        print("Login successful!")
    else:
        print("Invalid username or password. Please try again.")

def main():
    while True:
        print("\n1. Signup\n2. Login\n3. Quit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            signup()
        elif choice == '2':
            login()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

# Close the database connection when the program exits
db.close()
