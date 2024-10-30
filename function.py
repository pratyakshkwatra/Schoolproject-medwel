import mysql.connector
import time

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="admin",
    auth_plugin="mysql_native_password",
)
cursor = conn.cursor()




def save_doctor_id(user_id, doctor_id):
    query = "INSERT INTO medical (id, doctors) VALUES (%s, %s) ON DUPLICATE KEY UPDATE doctors = %s"
    cursor.execute(query, (user_id, doctor_id, doctor_id))
    conn.commit()

def send_message(sender_id, recipient_id, message_text):
    query = "INSERT INTO messages (sender_id, recipient_id, message_text) VALUES (%s, %s, %s)"
    cursor.execute(query, (sender_id, recipient_id, message_text))
    cnx.commit()

def get_messages(user_id):
    query = "SELECT * FROM messages WHERE recipient_id = %s"
    cursor.execute(query, (user_id,))
    messages = cursor.fetchall()
    return messages
    
def get_user_role(username):
    query = "SELECT role FROM users WHERE username = %s"
    cursor.execute(query, (username,))
    result = cursor.fetchone()
    if result:
        return result[0]  
    else:
        return None
def notif_grab(username):
    query = "SELECT notifs FROM users WHERE username = %s"
    cursor.execute(query, (username,))
    result = cursor.fetchone()
    if result:
        
        return result[0]  
    else:
        return None
def update_user_first_value(username, new_value):

    query = "UPDATE users SET first = %s WHERE username = %s"
    cursor.execute(query, (new_value, username))

    conn.commit()
    print(f"Updated first value for user {username} to {new_value}")   
def get_user_first_value(username):
    query = "SELECT first FROM users WHERE username = %s"
    cursor.execute(query, (username,))
    result = cursor.fetchone()
    if result:
        
        return result[0]  # Return the value of the "1st" column
    else:
        return None 
def check_username_exists(username):
    query = "SELECT COUNT(*) FROM users WHERE username = %s"
    cursor.execute(query, (username,))
    count = cursor.fetchone()[0]
    return count > 0
def check_email_exists(email):
    query = "SELECT COUNT(*) FROM users WHERE email = %s"
    cursor.execute(query, (email,))
    count = cursor.fetchone()[0]
    return count > 0
def create_account():
    username = input("Enter a username: ")
    if check_username_exists(username):
        print("Username already exists. Please choose a different username.")
        time.sleep(1)
        print("\n \n")
        time.sleep(1)
        return
    password = input("Enter a password: ")
    email = input("Enter an email: ")
    if check_email_exists(email):
        print("Email already exists. Please choose a different email.")
        time.sleep(1)
        print("\n \n")
        time.sleep(1)
        return
    area = input("enter your pincode")
    time.sleep(1)
    print("\n registering user \n")
    time.sleep(2)
    cursor.execute("""
        INSERT INTO users (username, password, email, area)
        VALUES (%s, %s, %s, %s)
    """, (username, password, email, area))
    print(" succesful \n")
    conn.commit()
def login():
    global username
    username = input("Enter your username: ")
    password = input("Enter your password: ")  
    global user
    cursor.execute("""
        SELECT * FROM users
        WHERE username = %s AND password = %s
    """, (username, password))
    user = cursor.fetchone()
def delete_account(username):
    query = "DELETE FROM users WHERE username = %s"
    cursor.execute(query, (username,))

    conn.commit()
    print(f"Account for {username} deleted successfully!")
def get_user_id(username):
    cursor.execute("SELECT id FROM users WHERE username = %s", (username,))
    result = cursor.fetchone()
    if result:
        return result[0]  
def get_doctor_info(doctor_id):
    query = "SELECT username,role,email FROM users WHERE id = %s AND role = 'doctor'"
    cursor.execute(query, (doctor_id,))
    doctor_info = cursor.fetchone()
    return doctor_info
def doctor_list(pin):
     query = "SELECT username,role,email,area FROM users WHERE area = %s AND role = 'doctor' "
     cursor.execute(query,(pin,))
     doctor_info = cursor.fetchall()
     return doctor_info 
def new_email(new):
    print("feature still in development ")
def display_messages_with_senders(user_id):
    query = """
    SELECT m.message_text, m.created_at, u.username 
    FROM messages m 
    JOIN users u ON m.sender_id = u.id 
    WHERE m.recipient_id = %s
    ORDER BY m.created_at DESC
    """
    cursor.execute(query, (user_id,))
    messages = cursor.fetchall()
    
    if not messages:
        print("\nNo messages found.\n")
        time.sleep(2)
        return

    for message in messages:
        message_text, created_at, sender_username = message
        print(f"[{created_at}] {sender_username}: {message_text}")
def send_message(sender_id, recipient_id, message_text):
    query = "INSERT INTO messages (sender_id, recipient_id, message_text) VALUES (%s, %s, %s)"
    cursor.execute(query, (sender_id, recipient_id, message_text))
    conn.commit()
    print("Message sent successfully!")   