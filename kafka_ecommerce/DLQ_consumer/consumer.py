from kafka import KafkaConsumer

consumer = KafkaConsumer(
    'dead_letter',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='inventory-dlq-group'
)

for message in consumer:
    # Process the dead letter message (e.g., log it, send an alert, etc.)
    print(f"Received dead letter message: {message.value.decode('utf-8')}")

    # Log these into an err file
    with open("DLQ_consumer/error.log", "a") as err_file:
        err_file.write(f"Dead letter message: {message.value.decode('utf-8')}\n")


