from kafka import KafkaConsumer, KafkaProducer
import random

consumer = KafkaConsumer(
    'orders',
    bootstrap_servers=['localhost:9092'],
    ## Available options : earliest / latest
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    ## Consumer group ID
    group_id='payment-group'
)

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092']
)

for message in consumer:
    print(f"Received message: {message.value.decode('utf-8')}")
    # Process the order message (e.g., handle payment)
    flag = random.choice([True, False])
    if flag:
        print("Payment processed successfully.")
    else:
        print("Payment processing failed.")
        ## Add a retry logic for a max of 3 times..
        retries = 0
        while retries < 1:
            print("Retrying payment...")
            flag = random.choice([True, False])
            if flag:
                print("Payment processed successfully on retry.")
                break
            retries += 1
        
        if retries == 1:
            print("Max tries reached, while trying to process payment.")
            print("Sending to dead letter queue.")
            producer.send('dead_letter', message.value)




