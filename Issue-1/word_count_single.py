import time
files = ["500MBfile.txt", "1GBfile.txt", "2GBfile.txt"]

for file in files:
    ## Also calculate the time per file
    start_time = time.time()
    word_count = {}
    with open(file, "r") as f:
        for line in f:
            words = line.split()
            for word in words:
                word_count[word] = word_count.get(word,0)+1

    print(f"Word count for {file}: {len(word_count)} unique words")
    print(f"Time taken to process {file}: {time.time() - start_time} seconds")
