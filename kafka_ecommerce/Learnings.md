* JMX :

Java Management Extensions (JMX) is a Java technology for monitoring and managing Java applications, system objects, devices, and services.

It gives you a standard way to expose runtime metrics, configuration, and operations of your Java app.

Commonly used in Java EE servers, JVM monitoring (heap, threads), and libraries like Kafka, ActiveMQ, Cassandra, etc.

Think of JMX as a management and monitoring framework for Java apps.

* MBean

An MBean (Managed Bean) is a Java object that exposes certain attributes and operations for management through JMX.

MBeans are registered in an MBeanServer (a kind of registry).

External tools (like jconsole, jvisualvm, or custom apps) can connect to this server to read and modify attributes or invoke methods.

*** These are all the Kafka MBeans Available
https://docs.confluent.io/platform/current/kafka/monitoring.html#kafka-monitoring-metrics-broker

*** Prometheus Client library
https://prometheus.io/docs/instrumenting/clientlibs/


*** FastApi
https://fastapi.tiangolo.com/async/
