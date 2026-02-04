# Lab 5: Mini-MapReduce on Amazon EMR

This repository contains the implementation of a distributed **MapReduce WordCount** job executed on an **Amazon Elastic MapReduce (EMR)** cluster.  
The project demonstrates the processing of a large text dataset using **Hadoop Streaming with Python**.

---

## 📋 Lab Objectives

- Run a MapReduce job on a managed Hadoop cluster (Amazon EMR).
- Use HDFS (Hadoop Distributed File System) for data storage.
- Analyze the performance and scalability of the cluster by resizing worker nodes.
- Demonstrate fault tolerance and parallel execution.

---

## 🛠 Technology Stack

- **Cloud Provider:** Amazon AWS  
- **Service:** Amazon EMR (Elastic MapReduce)  
- **Framework:** Hadoop Streaming  
- **Language:** Python 3  
- **Instance Type:** m4.large (1 Master, 2–4 Core Nodes)

---

## 📂 Repository Structure

- `mapper.py` – Python script that reads input from `STDIN`, tokenizes text, and emits key-value pairs (`word \t 1`)
- `reducer.py` – Python script that aggregates key-value pairs from `STDIN` and calculates total word counts
- `README.md` – Project documentation and experiment results

---

## 📊 Dataset

The project uses a sample dump of the **Simple English Wikipedia**.

- **Source:** [Dump of Simple English Wiki](https://github.com/LGDoor/Dump-of-Simple-English-Wiki)
- **File:** `corpus.txt`
- **Location in HDFS:** `/user/hadoop/input/`

---

## 🚀 How to Run

### 1. Connect to EMR Master Node

```bash
ssh -i your-key.pem hadoop@ec2-xx-xx-xx-xx.compute-1.amazonaws.com
2. Download and Upload Data to HDFS
bash
Copy code
wget https://github.com/LGDoor/Dump-of-Simple-English-Wiki/raw/refs/heads/master/corpus.tgz
tar -xvzf corpus.tgz

hdfs dfs -mkdir -p /user/hadoop/input
hdfs dfs -put corpus.txt /user/hadoop/input/
3. Run the MapReduce Job
bash
Copy code
hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
  -files mapper.py,reducer.py \
  -mapper mapper.py \
  -reducer reducer.py \
  -input /user/hadoop/input/ \
  -output /user/hadoop/output/
4. View Results
bash
Copy code
hdfs dfs -head /user/hadoop/output/part-00000
🧪 Experiment: Scaling Scenario
A scaling experiment was performed to verify that increasing the number of worker nodes reduces execution time due to parallel processing.

Scenario A: 2 Core Nodes vs 4 Core Nodes
Configuration	Number of Core Nodes	Execution Time	Performance Gain
Baseline	2 Nodes	55 seconds	–
Scaled	4 Nodes	45 seconds	~18% faster

Observation
Scaling the cluster from 2 to 4 core nodes reduced the processing time from 55 seconds to 45 seconds.
This confirms that the MapReduce framework efficiently utilizes additional resources to parallelize the Map phase, improving overall job performance.

Author: Your Name
Date: February 2026
