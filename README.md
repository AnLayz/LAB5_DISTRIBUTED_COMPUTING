# Lab 5: Mini-MapReduce on Amazon EMR

This repository contains the code and configuration for running a MapReduce WordCount job on a managed Hadoop cluster using Amazon Elastic MapReduce (EMR).

## 📌 Project Overview
- **Objective:** Run a distributed MapReduce job on a large dataset using AWS EMR.
- **Platform:** Amazon EMR (Hadoop Streaming).
- **Language:** Python 3.
- **Dataset:** Simple English Wikipedia Dump.

## 📂 Files
- `mapper.py`: Reads input from STDIN, splits lines into words, and emits `word \t 1`.
- `reducer.py`: Reads key-value pairs from STDIN, aggregates counts, and emits final word counts.

## 📊 Dataset
Used a subset of the Wikipedia text dump.
- **Source:** [Dump of Simple English Wiki](https://github.com/LGDoor/Dump-of-Simple-English-Wiki)
- **File:** `corpus.txt` uploaded to HDFS at `/user/hadoop/input/`

## 🚀 How to Run
To execute the job on the EMR Master Node, use the following command:

```bash
hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
    -files mapper.py,reducer.py \
    -mapper mapper.py \
    -reducer reducer.py \
    -input /user/hadoop/input/ \
    -output /user/hadoop/output/