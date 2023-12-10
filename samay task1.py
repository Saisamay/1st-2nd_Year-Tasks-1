from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

# Replace these with a more secure storage mechanism in a real application
user_credentials = {}

def encrypt_password(password, salt):
    cipher = AES.new(salt, AES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(password, AES.block_size))
    return cipher.iv + ciphertext

def decrypt_password(encrypted_data, salt):
    cipher = AES.new(salt, AES.MODE_CBC, iv=encrypted_data[:16])
    decrypted = unpad(cipher.decrypt(encrypted_data[16:]), AES.block_size)
    return decrypted

def register(username, password):
    if username not in user_credentials:
        salt = get_random_bytes(16)
        encrypted_password = encrypt_password(password.encode('utf-8'), salt)
        user_credentials[username] = {'password': encrypted_password, 'salt': salt}
        print(f"User '{username}' registered successfully!")
        return True
    else:
        print(f"User '{username}' already exists. Choose a different username.")
        return False

def login(username, password):
    if username in user_credentials:
        stored_password = user_credentials[username]['password']
        salt = user_credentials[username]['salt']
        entered_password = encrypt_password(password.encode('utf-8'), salt)

        if entered_password == stored_password:
            print("Login successful!")
            return True
        else:
            print("Login failed. Incorrect password.")
    else:
        print("Login failed. User not registered.")

    return False

# Example usage:
username_input = input("Enter your username: ")
password_input = input("Enter your password: ")

if not login(username_input, password_input):
    # If login fails, register the user
    register_choice = input("User not registered. Do you want to register? (yes/no): ").lower()
    if register_choice == 'yes':
        register_password = input("Enter your password for registration: ")
        register(username_input, register_password)
    else:
        print("Goodbye!")

    
