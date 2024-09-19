import socket
import random

def main():
    # Connect to the server
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sc:
        sc.connect(('localhost', 6017))
        
        # Get input from the user
        s = input("Enter the string: ")
        
        # Initialize variables
        key = []
        ct = ''
        
        # Encrypt the message
        for char in s:
            j = random.randint(0, 49)  # Random integer between 0 and 49
            key.append(str(j))          # Append to key list
            ct += chr(ord(char) + j)   # Encrypt character

            print(f"j={j}")             # Print the random number used for each character
            
        # Convert key list to a comma-separated string
        key_str = ','.join(key)
        
        # Print the key and encrypted message
        print(f"Key={key_str}")
        print(f"Encrypted message: {ct}")
        
        # Send the encrypted message and key
        message = f"{ct},{key_str}"
        sc.sendall(message.encode('utf-8'))  # Send as bytes

if __name__ == "__main__":
    main()
