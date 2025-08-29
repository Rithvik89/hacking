import time
from kafka import KafkaConsumer
from pydantic import BaseModel
import threading

inventory = {}

## Order model
class Order(BaseModel):
    order_id: int
    user_id: int
    product_id: int
    quantity: int


## Log inventory metrics thread .
def log_metrics():
    while True:
        time.sleep(60)
        print("Current inventory levels:")
        for order_id, quantity in inventory.items():
            print(f"  Order ID {order_id}: Quantity {quantity}")

metrics_thread = threading.Thread(target=log_metrics, daemon=True)
metrics_thread.start()

## Start a different thread for DLQ messages and update the inventory accordingly .

consumer_DLQ = KafkaConsumer(
    'dead_letter',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='inventory-group'
)

def process_dlq_messages():
    for message in consumer_DLQ:
        print(f"Received DLQ message: {message.value.decode('utf-8')}")
        # Process the dead letter message (e.g., log it, send an alert, etc.)
        order = message.value.decode('utf-8')
        order_data = Order.model_validate_json(order)

        inventory[order_data.order_id] = inventory.get(order_data.order_id, 0) - 1

        print(f"Updated inventory for the failed transactions in DLQ: {inventory}")

dlq_thread = threading.Thread(target=process_dlq_messages, daemon=True)
dlq_thread.start()

consumer = KafkaConsumer(
    'orders',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='inventory-group'
)

for message in consumer:
    print(f"Received message: {message.value.decode('utf-8')}")
    # Process the inventory message (e.g., update stock levels)
    order = message.value.decode('utf-8')
    order_data = Order.model_validate_json(order)

    inventory[order_data.order_id] = inventory.get(order_data.order_id, 0) + 1

    print(f"Updated inventory: {inventory}")




