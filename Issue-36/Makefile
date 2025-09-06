## Local Mode setup.

local:
	.venv/bin/pyspark --master local[2] --name "LocalPySpark"

## Standalone mode setup.

start-worker:
	@if [ -z "$(id)" ]; then \
		echo "Usage: make start-worker id=<worker_id>"; \
		exit 1; \
	fi; \
	docker run -d \
	--name=spark-worker$${id} \
	--network=spark-net \
	-e SPARK_MASTER_URL=spark://spark-master:7077 \
	-e SPARK_MODE=worker \
	-v /Users/rithvik/Documents/hackathons/Issue-36:/data \
	bitnami/spark

start-master:
	docker run -d \
	--name=spark-master \
	--network=spark-net \
	-e SPARK_MODE=master \
	-p 8080:8080 \
	-p 7077:7077 \
	-v /Users/rithvik/Documents/hackathons/Issue-36:/data \
	bitnami/spark

stop-master:
	docker rm -f spark-master || true

stop-worker:
	@if [ -z "$(id)" ]; then \
		echo "Usage: make stop-worker id=<worker_id>"; \
		exit 1; \
	fi; \
	docker rm -f spark-worker$${id} || true

## Some issue with pyspark shell opeing in docker container in client mode and standalone cluster manager.
## So, use scala shell for now.
pyspark-shell:
	docker run -it --rm \
	--network spark-net \
	-v /Users/rithvik/Documents/hackathons/Issue-36:/data \
	bitnami/spark:latest \
	pyspark --master spark://spark-master:7077

scala-shell:
	docker run -it --rm \
	--network spark-net \
	-p 4040:4040 \
	bitnami/spark:latest \
	spark-shell --master spark://spark-master:7077

