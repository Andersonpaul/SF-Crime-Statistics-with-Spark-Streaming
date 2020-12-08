# SF-Crime-Statistics-with-Spark-Streaming
This repository contains the project artefacts for the Nano-Degree Programme in Data Streaming by Udacity

Question: How did changing values on the SparkSession property parameters affect the throughput and latency of the data?

As like any standard streaming system or platform, as latency increases throughput is reduced. Next batch will take longer to be processed and the overall throughput decreases.

Question: What were the 2-3 most efficient SparkSession property key/value pairs? Through testing multiple variations on values, how can you tell these were the most optimal?

Possible properties: spark.default.parallelism, spark.streaming.kafka.maxRatePerPartition

Results can be seen in Spark Progress Report (inputRowsPerSecond or processedRowsPerSecond) or in Spark UI Streaming page (Min, Median and Max rate of records/second).
