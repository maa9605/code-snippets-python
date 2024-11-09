import socket
import ssl

SERVER_HOST = "127.0.0.1"
SERVER_PORT = 60000

HOST = "127.0.0.1"
PORT = 60002

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

#client = ssl.wrap_socket(client, keyfile="key.pem", certfile="cert.pem")

def send_message(message):
    
    msg = message.encode("utf-8")
    client.send(msg)

if __name__ == "__main__":
    client.bind((HOST, PORT))
    client.connect((SERVER_HOST, SERVER_PORT))

    while True:
        from time import sleep
        
        send_message("Hello")
        msg = client.recv(1024)
        print(msg.decode('utf-8'))
        sleep(1)
