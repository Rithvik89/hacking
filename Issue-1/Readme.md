# 📝 Spark Word Count Performance Challenge

## 🎯 Objective
Implement the classic word count problem using both Spark (RDDs or DataFrames) and a single-threaded Python solution. Compare their performance, scalability, and efficiency.

---

## ✅ Checklist

### Data Preparation
- [ ] Download a large text file (e.g., Project Gutenberg book, Wikipedia dump)
- [*] Prepare multiple file sizes (10MB, 100MB, 1GB)

### Implementation
- [*] Implement single-threaded Python word count (`word_count_single.py`)
- [*] Implement Spark word count using RDDs or DataFrames (`word_count_spark.py`)

### Performance Comparison
- [*] Measure execution time for both solutions
- [*] Test with increasing file sizes
- [ ] Document CPU and memory usage (optional)

### Scalability & Efficiency Analysis
- [*] Summarize results in a table or chart
- [*] Analyze Spark's distributed computation vs. single-threaded bottlenecks
- [ ] Write a brief analysis of when to use Spark vs. single-threaded solutions

### Documentation
- [ ] Create `results.md` with performance comparison, charts, and analysis
- [ ] Add code samples and instructions for running both solutions

---

## 🛠️ Steps

1. **Prepare a Large Text File**
   - Download a dataset and split into different sizes for testing.

2. **Single-Threaded Solution**
   - Write a Python script that reads the file and counts word frequencies using a dictionary.

3. **Spark Solution**
   - Use PySpark to implement word count with RDDs or DataFrames.
   - Run the job locally or on a cluster.

4. **Performance Comparison**
   - Measure execution time for both solutions.
   - Test with increasing file sizes.
   - Document CPU and memory usage if possible.

5. **Scalability & Efficiency**
   - Discuss how Spark distributes computation across nodes and handles large datasets.
   - Highlight bottlenecks in the single-threaded approach (e.g., memory limits, CPU saturation).

6. **Documentation**
   - Summarize results in a table or chart.
   - Write a brief analysis of when to use Spark vs. single-threaded solutions.

---

## 💡 Tips
- Use Python's `time` module or Spark's built-in metrics for benchmarking.
- For Spark, test both local and cluster modes if possible.
- Visualize results with charts for clarity.

---
