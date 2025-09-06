For this task we installed python 3.12.xx and created a virtual environment using the command:
```bash
```bash
/opt/homebrew/bin/python3.12 -m venv .venv
```

To ensure compatibility between the Spark driver and worker, Python 3.12.x was installed and a dedicated virtual environment was created:

```bash
pyspark --master spark://localhost:7077
```
And i tried performing few computation in the cluster, I got the following error:


an error occurred during computation:
pyspark.errors.exceptions.base.PySparkRuntimeError: [PYTHON_VERSION_MISMATCH] Python in worker has different version: 3.12 than that in driver: 3.13, PySpark cannot run with different minor versions.
Please check environment variables PYSPARK_PYTHON and PYSPARK_DRIVER_PYTHON are correctly set.
pyspark.errors.exceptions.base.PySparkRuntimeError: [PYTHON_VERSION_MISMATCH] Python in worker has different version: 3.12 than that in driver: 3.13, PySpark cannot run with different minor versions.
Please check environment variables PYSPARK_PYTHON and PYSPARK_DRIVER_PYTHON are correctly set.
```

**Background:**

When connecting to a standalone Spark cluster with:

```bash
```
```
**Solution:**

Created a new virtual environment using Python 3.12 and ensured both the Spark driver and worker use the same Python version. This resolved the version mismatch error.
To fix this, I create a new venv for this task and made sure that both the driver and worker use the same python version 



