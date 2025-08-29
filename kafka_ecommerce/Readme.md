# 🛒 Kafka E-Commerce Mini-Pipeline Hackathon

## 📜 Challenge Narrative
Your team is building the backend infrastructure for a growing **e-commerce startup**.  
All core activities—**orders, payments, and inventory updates**—must now flow through a **Kafka-based event pipeline** to ensure scalability and fault tolerance.

You have **4 hours** to design, implement, and operate this pipeline **end-to-end**.  
You will act as both:  
1. A **Kafka developer** (writing producers/consumers and services).  
2. A **Kafka administrator** (managing clusters, topics, and monitoring).

The goal is to simulate a **real-world scenario** where you handle rapid development, operations, and troubleshooting in a time-constrained hackathon environment.

---

## 🏗️ System Requirements

### Core Requirements
1. **Kafka Cluster**
   - Deploy a **3-broker Kafka cluster** with ZooKeeper or KRaft mode using Docker Compose.
   - Create the following Kafka topics:
     - `orders`: All incoming customer orders.
     - `dead_letter`: Stores failed or undeliverable events.

2. **Producer Service**
   - Build a REST API `POST /order`:
     - Accepts a JSON payload for a new order.
     - Publishes the order event to the `orders` topic.
     - Include fields like `order_id`, `user_id`, `product_id`, `quantity`.

3. **Payment Consumer**
   - Reads messages from the `orders` topic.
   - Simulates payment processing:
     - Randomly fail some transactions.
     - If a message fails processing after retries, publish it to `dead_letter`.
     - If a message fails processing after retries, it is published to the `dead_letter` topic.
     - **Note:** If payment processing fails and the message is sent to the `dead_letter` topic, the inventory should **not** be updated. Inventory updates only occur for successfully processed orders.

4. **Inventory Consumer**
   - Reads messages from the `orders` topic.
   - Maintains an **in-memory count of inventory sold per product**.
   - Logs summary metrics every minute (total items sold per product).

5. **Dead Letter Queue (DLQ) Consumer**
   - Reads messages from `dead_letter` topic.
   - Prints them to logs or stores in a file for debugging.

---

### Monitoring Requirements
- Deploy **Prometheus JMX Exporter** for Kafka brokers.
- Import a **Grafana Kafka dashboard** (pre-built template allowed).
- Must track:
  - Broker health
  - Topic throughput (messages in/out per second)
  - Consumer lag

---

### Operational Challenges
Perform the following operations and record results:
1. **Broker Failure Simulation**
   - Stop one broker.
   - Observe and record consumer lag changes.
   - Restart broker and verify recovery.

2. **Partition Reassignment**
   - Add a **4th broker**.
   - Trigger a **partition reassignment** and verify load balancing.

---

## ✅ Expected Deliverables

1. **Cluster Setup**
   - `docker-compose.yml` for a 3-broker Kafka cluster.
   - Scripts or commands for topic creation.

2. **Producer**
   - REST API endpoint to submit orders.
   - Publishes messages to `orders` topic.

3. **Consumers**
   - Payment Consumer with error handling and DLQ logic.
   - Inventory Consumer that aggregates and logs item counts.
   - DLQ Consumer for error monitoring.

4. **Monitoring**
   - Grafana dashboard with key metrics (broker health, topic throughput, consumer lag).
   - Screenshots included in your submission.

5. **Ops Simulations**
   - Broker failure simulation report (observations, lag, recovery).
   - Partition reassignment test with 4th broker.

6. **Documentation**
   - README with:
     - Setup instructions (cluster, services, dashboards).
     - Architecture diagram.
     - Screenshots of working system.
     - Lessons learned.

---

## 🔥 Stretch Goals (Optional if Time Allows)
- Implement a Kafka Streams application to compute rolling metrics (orders per product in a 10-minute window).
- Introduce schema validation with Confluent Schema Registry.
- Add SASL/PLAIN authentication and topic-level ACLs.

---

## 🧰 Tech Stack
- **Kafka**: Apache Kafka 3.x
- **Containerization**: Docker + Docker Compose
- **Language**: Java (Spring Boot) or Python (FastAPI)
- **Monitoring**: Prometheus JMX Exporter, Grafana
- **CLI Tools**: Kafka CLI scripts for admin ops

---

## 🎯 Success Criteria
You succeed if, in **4 hours**:
1. The Kafka cluster is running with multiple brokers and required topics.
2. You can:
   - Send an order using your API.
   - See it consumed and processed.
   - See failed messages routed to the DLQ.
3. Grafana shows **real-time Kafka metrics**.
4. You simulate a **broker crash** and see lag and recovery in action.
5. You document your setup, share screenshots, and reflect on improvements.

---



