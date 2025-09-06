
# Apache Spark Job Submission Guide

This guide explains how to submit jobs to Apache Spark using `spark-submit`, describes deployment modes, and details the most common cluster managers.

---

## 🚀 Spark Job Submission Syntax

```bash
./bin/spark-submit \
  --class <main-class> \
  --master <master-url> \
  --deploy-mode <deploy-mode> \
  --conf <key>=<value> \
  ... # other options \
  <application-jar> \
  [application-arguments]
```

### Argument Reference

| Argument                | Description                                                                 |
|-------------------------|-----------------------------------------------------------------------------|
| `--class <main-class>`  | Entry point for your application (main class)                               |
| `--master <master-url>` | Cluster manager to connect to (local, YARN, Mesos, Standalone, Kubernetes)  |
| `--deploy-mode`         | Where to run the driver: `client` (local) or `cluster` (on cluster node)    |
| `--conf <key>=<value>`  | Set Spark configuration properties                                          |
| `<application-jar>`     | Path to your application's JAR or Python script                             |
| `[application-arguments]`| Arguments for your application                                              |

---

## 🖥️ Deployment Modes in Spark

### Client Mode
The Spark driver runs on the machine where you submit the job. Suitable for development and debugging.

```bash
./bin/spark-submit \
  --class <main-class> \
  --master <master-url> \
  --deploy-mode client \
  --executor-memory 20G \
  --num-executors 50 \
  /path/to/examples.jar \
  1000
```

### Cluster Mode
The Spark driver runs on a worker node in the cluster. Recommended for production and large-scale jobs.

```bash
./bin/spark-submit \
  --class <main-class> \
  --master <master-url> \
  --deploy-mode cluster \
  --executor-memory 20G \
  --num-executors 50 \
  /path/to/examples.jar \
  1000
```

---

## 🏢 Cluster Managers in Spark

| Cluster Manager         | Master URL Example                      | Notes                                      |
|------------------------|-----------------------------------------|--------------------------------------------|
| Standalone             | `spark://207.184.161.138:7077`          | Built-in, easy setup for small/medium jobs  |
| Local                  | `local[8]`                              | For development/testing on local machine    |
| YARN                   | `yarn`                                  | Hadoop ecosystem, resource management       |
| Mesos                  | `mesos://host:port`                     | General-purpose, fine-grained sharing       |
| Kubernetes             | `k8s://https://<k8s-master>:<port>`     | Container orchestration, cloud-native       |

### Example Commands

**Standalone Cluster:**
```bash
./bin/spark-submit \
  --class <main-class> \
  --master spark://207.184.161.138:7077 \
  --deploy-mode <deploy-mode> \
  --executor-memory 20G \
  --total-executor-cores 100 \
  /path/to/examples.jar \
  1000
```

**Local Mode:**
```bash
./bin/spark-submit \
  --class <main-class> \
  --master "local[8]" \
  /path/to/examples.jar \
  100
```

**YARN:**
```bash
./bin/spark-submit \
  --class <main-class> \
  --master yarn \
  --deploy-mode <deploy-mode> \
  --executor-memory 20G \
  --num-executors 50 \
  /path/to/examples.jar \
  1000
```

**Mesos:**
```bash
# Example (fill in host/port as needed)
./bin/spark-submit \
  --class <main-class> \
  --master mesos://host:port \
  ...
```

**Kubernetes:**
```bash
# Example (fill in k8s master and port)
./bin/spark-submit \
  --class <main-class> \
  --master k8s://https://<k8s-master>:<port> \
  ...
```


## 📊 Monitoring Spark Applications

Spark provides several dashboards for monitoring and managing your applications:

- **Spark UI**: The default web interface, available at `http://<driver-node>:4040` while your application is running. It displays:
  - Job and stage progress
  - Task execution details
  - Storage usage
  - Environment and configuration
  - Executor information

- **Spark Master UI** (Standalone mode):
  - Access at `http://<master-node>:8080` when using a standalone Spark cluster.
  - Shows cluster status, active workers, and running applications.
  - In cluster mode, other cluster managers (YARN, Mesos) provide their own UIs for monitoring drivers, workers, and application status.


> **Note:**
> - Port `7077` is the default for the Spark standalone cluster manager (for worker/master communication).
> - The Spark UI (`4040`) is only available while the application is running.
> - In Spark Local mode, there is only a single process that is both the driver and executor, And all the master responsibilities are handled by driver itself. Tho achieve parallelism, multiple threads are spawned within the same process (for Executors).





