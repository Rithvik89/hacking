from fastapi import FastAPI
from pydantic import BaseModel
from kafka import KafkaProducer, KafkaConsumer

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092']
)



app = FastAPI()

class Order(BaseModel):
    order_id: int
    user_id: int
    product_id: int
    quantity: int

@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.post("/order")
def create_order(order: Order):
    # Publish the order details to kafka topic.
    producer.send('orders', order.json().encode('utf-8'))
    return {"status": "order", "order": order}
