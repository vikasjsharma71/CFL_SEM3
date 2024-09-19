import socket

def main():
    # Create a server socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind(('localhost', 6017))
        server_socket.listen(1)  # Listen for incoming connections
        print("Waiting for a connection...")
        
        # Accept a connection
        conn, addr = server_socket.accept()
        with conn:
            print(f"Connected by {addr}")
            
            # Read the incoming data
            ct = conn.recv(1024).decode('utf-8')  # Buffer size is 1024 bytes
            s = ct.split(",")  # Split the message and key
            encrypted_message = s[0]
            key = list(map(int, s[1:]))  # Convert key strings to integers
            
            print(f"Encrypted message: {encrypted_message}")
            
            # Decrypt the message
            pt = ''
            for i in range(len(encrypted_message)):
                j = key[i]
                pt += chr(ord(encrypted_message[i]) - j)  # Decrypt character
                print(f"Key={j}")

            print(f"Message from Sender: {pt}")

if __name__ == "__main__":
    main()
