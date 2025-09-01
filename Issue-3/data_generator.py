import random
from model import Message
import socket
import json

Senders = ["Alice", "Bob", "Charlie"]
Recipients = ["David", "Eve", "Frank"]
Contents = ["Hello!", "How are you?", "Goodbye!"]

def generate_message() -> Message:
    sender = Senders[random.randint(1,len(Senders))-1]
    recipient = Recipients[random.randint(1,len(Recipients))-1]
    content = Contents[random.randint(1,len(Contents))-1]    

    return Message(sender=sender, recipient=recipient, content=content)

## Send Messages into the socket 2 messages per-second.

HOST = 'localhost'
PORT = 8080

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.connect((HOST,PORT))
    print(f"Connected to socket {HOST}:{PORT}")
    while True:
        msg = generate_message()
        bytes = msg.json().encode()
        s.sendall(bytes)
        print(f"Message sent: {msg.content}")


